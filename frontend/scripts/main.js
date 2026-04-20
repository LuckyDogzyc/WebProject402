import Phaser from 'phaser';
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
    new Phaser.Game(config);
});
