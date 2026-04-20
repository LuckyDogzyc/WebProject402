export default class Character extends Phaser.Physics.Arcade.Sprite {
    constructor(scene, x, y, memberData) {
        super(scene, x, y, memberData.id);
        
        this.memberData = memberData;
        this.characterId = memberData.id;
        this.characterName = memberData.name;
        this.currentState = 'idle';
        this.interactive = true;
        
        // 启用物理
        scene.physics.add.existing(this);
        this.setCollideWorldBounds(true);
        
        // 设置交互
        this.setInteractive();
        
        // 绑定事件
        this.on('pointerdown', this.handleClick, this);
        this.on('pointerover', this.handleHover, this);
        this.on('pointerout', this.handleHoverOut, this);
        
        // 添加到场景
        scene.add.existing(this);
        
        // 播放待机动画
        this.play(`${this.characterId}_idle`);
        
        // 添加名称标签
        this.createNameLabel();
    }

    createNameLabel() {
        const nameText = this.scene.add.text(
            this.x,
            this.y - 30,
            this.characterName,
            {
                fontSize: '14px',
                fill: '#fff',
                backgroundColor: 'rgba(0,0,0,0.5)',
                padding: { x: 5, y: 2 }
            }
        );
        nameText.setOrigin(0.5);
        
        // 保存引用
        this.nameLabel = nameText;
    }

    handleClick() {
        console.log(`👆 点击角色: ${this.characterName}`);
        this.showInteractionMenu();
    }

    handleHover() {
        this.scene.tweens.add({
            targets: this,
            scaleX: 1.1,
            scaleY: 1.1,
            duration: 100
        });
    }

    handleHoverOut() {
        this.scene.tweens.add({
            targets: this,
            scaleX: 1,
            scaleY: 1,
            duration: 100
        });
    }

    showInteractionMenu() {
        const scene = this.scene;
        
        // 创建菜单容器
        const menu = scene.add.container(this.x, this.y - 80);
        
        // 背景
        const bg = scene.add.rectangle(0, 0, 180, 120, 0xffffff);
        bg.setStrokeStyle(2, 0x000000);
        menu.add(bg);
        
        // 标题
        const title = scene.add.text(0, -40, this.characterName, {
            fontSize: '16px',
            fill: '#000',
            fontStyle: 'bold'
        });
        title.setOrigin(0.5);
        menu.add(title);
        
        // 按钮
        const buttons = [
            { text: '🎯 调酒', action: () => this.makeDrink() },
            { text: '🍺 灌醉', action: () => this.getDrunk() },
            { text: 'ℹ️ 查看', action: () => this.showInfo() },
            { text: '❌ 关闭', action: () => menu.destroy() }
        ];
        
        buttons.forEach((btn, index) => {
            const x = -60 + (index % 2) * 120;
            const y = -10 + Math.floor(index / 2) * 30;
            
            const button = scene.add.text(x, y, btn.text, {
                fontSize: '14px',
                fill: '#000',
                backgroundColor: '#f0f0f0',
                padding: { x: 8, y: 4 }
            });
            button.setOrigin(0.5);
            button.setInteractive();
            button.on('pointerdown', btn.action);
            button.on('pointerover', () => button.setStyle({ backgroundColor: '#e0e0e0' }));
            button.on('pointerout', () => button.setStyle({ backgroundColor: '#f0f0f0' }));
            menu.add(button);
        });
        
        // 点击外部关闭
        const closeHandler = () => {
            menu.destroy();
            scene.input.off('pointerdown', closeHandler);
        };
        
        scene.time.delayedCall(5000, closeHandler);
    }

    async makeDrink() {
        console.log(`🍺 ${this.characterName} 正在调酒`);
        
        // 播放工作动画
        this.play(`${this.characterId}_work`);
        
        // 显示效果
        this.showEffect('🍹 调酒中...');
        
        // 3秒后恢复
        this.scene.time.delayedCall(3000, () => {
            this.play(`${this.characterId}_idle`);
        });
    }

    async getDrunk() {
        console.log(`🥴 ${this.characterName} 被灌醉了`);
        
        // 播放醉酒动画
        this.play(`${this.characterId}_drunk`);
        
        // 显示效果
        this.showEffect('🥴 醉酒了！');
        
        // 更新状态
        this.currentState = 'drunk';
        
        // 10秒后恢复
        this.scene.time.delayedCall(10000, () => {
            this.play(`${this.characterId}_idle`);
            this.currentState = 'idle';
            this.showEffect('😊 恢复清醒');
        });
    }

    showInfo() {
        const scene = this.scene;
        
        const infoText = `
        👤 名称: ${this.characterName}
        🎭 ID: ${this.characterId}
        ❤️ 状态: ${this.currentState}
        `.trim();
        
        const info = scene.add.text(
            this.x,
            this.y - 150,
            infoText,
            {
                fontSize: '12px',
                fill: '#000',
                backgroundColor: '#fff',
                padding: { x: 10, y: 10 },
                lineSpacing: 5
            }
        );
        info.setOrigin(0.5);
        
        scene.time.delayedCall(4000, () => info.destroy());
    }

    showEffect(text) {
        const scene = this.scene;
        const effectText = scene.add.text(
            this.x,
            this.y - 50,
            text,
            {
                fontSize: '14px',
                fill: '#fff',
                backgroundColor: '#000',
                padding: { x: 8, y: 4 }
            }
        );
        effectText.setOrigin(0.5);
        
        scene.tweens.add({
            targets: effectText,
            y: this.y - 80,
            alpha: 0,
            duration: 2000,
            onComplete: () => effectText.destroy()
        });
    }

    destroy() {
        if (this.nameLabel) {
            this.nameLabel.destroy();
        }
        super.destroy();
    }
}
