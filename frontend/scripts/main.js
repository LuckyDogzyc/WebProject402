import * as Phaser from '../node_modules/phaser/dist/phaser.esm.js';
import Boot from './scenes/Boot.js';
import Home from './scenes/Home.js';

const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    parent: 'game-container',
    backgroundColor: '#2c3e50',
    pixelArt: true,  // 关键：启用像素风
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 0 },  // 俯视图，无重力
            debug: false
        }
    },
    scene: [Boot, Home],
    scale: {
        mode: Phaser.Scale.FIT,
        autoCenter: Phaser.Scale.CENTER_BOTH
    }
};

// 启动游戏
window.addEventListener('load', () => {
    try {
        const game = new Phaser.Game(config);
        console.log('✅ Phaser 游戏启动成功');
    } catch (error) {
        console.error('❌ Phaser 启动失败:', error);
        document.getElementById('game-container').innerHTML = `
            <div style="color: white; text-align: center; padding: 50px;">
                <h2>❌ 游戏启动失败</h2>
                <p>${error.message}</p>
                <p>请查看浏览器控制台获取详细信息</p>
            </div>
        `;
    }
});
