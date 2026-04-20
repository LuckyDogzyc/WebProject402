// Boot.js - 启动场景
export default class Boot extends Phaser.Scene {
    constructor() {
        super({ key: 'Boot' });
    }

    preload() {
        console.log('🔄 开始加载资源...');

        // 创建加载进度条
        const progressBar = this.add.graphics();
        const width = this.cameras.main.width;
        const height = this.cameras.main.height;
        
        const progressBarBg = this.add.graphics();
        progressBarBg.fillStyle(0x333333, 1);
        progressBarBg.fillRect(width / 4, height / 2 - 15, width / 2, 30);
        
        this.load.on('progress', (value) => {
            progressBar.clear();
            progressBar.fillStyle(0x4CAF50, 1);
            progressBar.fillRect(width / 4, height / 2 - 15, (width / 2) * value, 30);
        });
        
        this.load.on('complete', () => {
            progressBar.destroy();
            progressBarBg.destroy();
            console.log('✅ 资源加载完成');
        });

        // 加载房间背景（占位符）
        try {
            this.load.image('room', 'assets/images/room.png');
        } catch (e) {
            console.warn('⚠️  无法加载房间背景，使用占位符');
        }
        
        // 为每个成员创建临时占位符
        const members = ['chu', 'bo', 'hao', 'qian', 'dong', 'zhu'];
        const colors = [0xFF6B6B, 0x4ECDC4, 0xFFE66D, 0x95E1D3, 0xF38181, 0xAA96DA];
        
        members.forEach((member, index) => {
            // 创建临时纹理（32x32 单帧）
            const graphics = this.make.graphics({ x: 0, y: 0, add: false });
            graphics.fillStyle(colors[index], 1);
            graphics.fillRect(0, 0, 32, 32);
            graphics.generateTexture(member, 32, 32);
            
            // 注册为精灵图（单帧）
            this.load.spritesheet(member, '__PHASER_GLOBAL_TEXTURE__' + member, {
                frameWidth: 32,
                frameHeight: 32
            });
        });
    }

    create() {
        console.log('🎮 创建动画...');

        // 创建全局动画
        this.createCharacterAnimations();
        
        // 显示启动信息
        console.log('✅ Phaser 3 初始化完成');
        
        // 延迟 1 秒后启动主场景
        this.time.delayedCall(1000, () => {
            console.log('🏠 启动主场景...');
            this.scene.start('Home');
        });
    }

    createCharacterAnimations() {
        const members = ['chu', 'bo', 'hao', 'qian', 'dong', 'zhu'];
        
        members.forEach(member => {
            // 待机动画（单帧循环）
            this.anims.create({
                key: `${member}_idle`,
                frames: [{ key: member, frame: 0 }],
                frameRate: 1,
                repeat: -1
            });

            // 行走动画（单帧）
            this.anims.create({
                key: `${member}_walk`,
                frames: [{ key: member, frame: 0 }],
                frameRate: 8,
                repeat: -1
            });

            // 工作动画（单帧）
            this.anims.create({
                key: `${member}_work`,
                frames: [{ key: member, frame: 0 }],
                frameRate: 8,
                repeat: -1
            });

            // 醉酒动画（单帧，慢速）
            this.anims.create({
                key: `${member}_drunk`,
                frames: [{ key: member, frame: 0 }],
                frameRate: 2,
                repeat: -1
            });
        });
        
        console.log('✅ 角色动画创建完成');
    }
}
