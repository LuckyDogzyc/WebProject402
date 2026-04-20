// Home.js - 主场景
import Character from '../objects/Character.js';

export default class Home extends Phaser.Scene {
    constructor() {
        super({ key: 'Home' });
    }

    create() {
        console.log('🏠 主场景加载');
        
        // 添加背景
        this.add.rectangle(400, 300, 800, 600, 0x2c3e50);
        
        // 创建标题
        this.add.text(400, 30, '402 虚拟生活社区系统', {
            fontSize: '32px',
            fill: '#fff',
            fontStyle: 'bold'
        }).setOrigin(0.5);
        
        // 创建角色组
        this.characters = this.physics.add.group();
        
        // 加载成员数据
        this.loadCharacters();
        
        // 创建UI
        this.createUI();
        
        // 欢迎消息
        this.showWelcomeMessage();
        
        console.log('✅ 主场景初始化完成');
    }

    async loadCharacters() {
        try {
            const response = await fetch('/api/members');
            const members = await response.json();
            
            console.log('📋 加载成员:', members);
            
            members.forEach((member, index) => {
                const x = 200 + (index % 3) * 200;
                const y = 200 + Math.floor(index / 3) * 200;
                
                const char = new Character(this, x, y, member);
                this.characters.add(char);
            });
            
            console.log(`✅ 创建了 ${members.length} 个角色`);
        } catch (error) {
            console.error('❌ 加载成员失败:', error);
            this.showError('无法加载成员数据');
        }
    }

    createUI() {
        // 音乐播放器按钮
        const musicBtn = this.add.text(700, 50, '🎵 音乐', {
            fontSize: '16px',
            backgroundColor: '#4CAF50',
            padding: { x: 10, y: 5 },
            color: '#fff'
        });
        musicBtn.setInteractive();
        musicBtn.on('pointerdown', () => this.showNotification('音乐播放器（开发中）'));
        
        // 聊天按钮
        const chatBtn = this.add.text(700, 100, '💬 聊天', {
            fontSize: '16px',
            backgroundColor: '#2196F3',
            padding: { x: 10, y: 5 },
            color: '#fff'
        });
        chatBtn.setInteractive();
        chatBtn.on('pointerdown', () => this.showNotification('聊天室（开发中）'));
        
        // 树洞按钮
        const treeHoleBtn = this.add.text(700, 150, '🌳 树洞', {
            fontSize: '16px',
            backgroundColor: '#FF9800',
            padding: { x: 10, y: 5 },
            color: '#fff'
        });
        treeHoleBtn.setInteractive();
        treeHoleBtn.on('pointerdown', () => this.showNotification('树洞（开发中）'));
        
        console.log('✅ UI 创建完成');
    }

    showNotification(message) {
        const notification = this.add.text(400, 550, message, {
            fontSize: '16px',
            backgroundColor: '#000',
            color: '#fff',
            padding: { x: 20, y: 10 }
        });
        notification.setOrigin(0.5);
        
        this.tweens.add({
            targets: notification,
            alpha: 0,
            y: 500,
            duration: 2000,
            delay: 2000,
            onComplete: () => notification.destroy()
        });
    }

    showWelcomeMessage() {
        const welcome = this.add.text(400, 300, '欢迎来到 402 虚拟生活社区系统！\n\nPhaser 3 引擎已启动\n像素风角色系统就绪\n\n试试点击角色进行互动', {
            fontSize: '18px',
            fill: '#fff',
            backgroundColor: 'rgba(0,0,0,0.7)',
            padding: { x: 30, y: 20 },
            align: 'center',
            lineSpacing: 8
        });
        welcome.setOrigin(0.5);
        
        // 5 秒后淡出
        this.tweens.add({
            targets: welcome,
            alpha: 0,
            duration: 1000,
            delay: 5000,
            onComplete: () => welcome.destroy()
        });
    }

    showError(message) {
        const error = this.add.text(400, 300, `❌ ${message}`, {
            fontSize: '20px',
            fill: '#ff0000',
            backgroundColor: 'rgba(0,0,0,0.8)',
            padding: { x: 20, y: 10 }
        });
        error.setOrigin(0.5);
        this.time.delayedCall(3000, () => error.destroy());
    }
}
