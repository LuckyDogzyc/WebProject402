/**
 * 402 虚拟生活社区系统 - 音乐播放器
 */

class MusicPlayer {
    constructor() {
        this.audio = new Audio();
        this.playlist = [];
        this.currentIndex = 0;
        this.isPlaying = false;
        this.isLooping = true;
        
        // 事件监听
        this.audio.addEventListener('ended', () => this.onTrackEnded());
        this.audio.addEventListener('loadedmetadata', () => this.onMetadataLoaded());
        this.audio.addEventListener('timeupdate', () => this.onTimeUpdate());
        this.audio.addEventListener('error', (e) => this.onError(e));
    }

    /**
     * 加载播放列表
     * @param {Array} tracks - 歌曲列表 [{title, url, artist}]
     */
    loadPlaylist(tracks) {
        this.playlist = tracks;
        if (tracks.length > 0) {
            this.loadTrack(0);
        }
    }

    /**
     * 加载指定曲目
     * @param {number} index - 曲目索引
     */
    loadTrack(index) {
        if (index >= 0 && index < this.playlist.length) {
            this.currentIndex = index;
            const track = this.playlist[index];
            this.audio.src = track.url;
            this.audio.load();
            
            // 更新 UI
            this.updateUI();
        }
    }

    /**
     * 播放
     */
    play() {
        this.audio.play().then(() => {
            this.isPlaying = true;
            this.updatePlayButton();
        }).catch(err => {
            console.error('播放失败:', err);
            this.showError('播放失败，请检查音频文件');
        });
    }

    /**
     * 暂停
     */
    pause() {
        this.audio.pause();
        this.isPlaying = false;
        this.updatePlayButton();
    }

    /**
     * 切换播放/暂停
     */
    toggle() {
        if (this.isPlaying) {
            this.pause();
        } else {
            this.play();
        }
    }

    /**
     * 下一首
     */
    next() {
        const nextIndex = (this.currentIndex + 1) % this.playlist.length;
        this.loadTrack(nextIndex);
        if (this.isPlaying) {
            this.play();
        }
    }

    /**
     * 上一首
     */
    prev() {
        const prevIndex = (this.currentIndex - 1 + this.playlist.length) % this.playlist.length;
        this.loadTrack(prevIndex);
        if (this.isPlaying) {
            this.play();
        }
    }

    /**
     * 跳转到指定时间
     * @param {number} time - 时间（秒）
     */
    seek(time) {
        this.audio.currentTime = time;
    }

    /**
     * 设置音量
     * @param {number} volume - 音量 (0.0 - 1.0)
     */
    setVolume(volume) {
        this.audio.volume = Math.max(0, Math.min(1, volume));
    }

    /**
     * 切换循环模式
     */
    toggleLoop() {
        this.isLooping = !this.isLooping;
        this.updateLoopButton();
    }

    /**
     * 曲目结束事件
     */
    onTrackEnded() {
        if (this.isLooping || this.currentIndex < this.playlist.length - 1) {
            this.next();
        } else {
            this.isPlaying = false;
            this.updatePlayButton();
        }
    }

    /**
     * 元数据加载完成
     */
    onMetadataLoaded() {
        const duration = this.audio.duration;
        this.updateDurationDisplay(duration);
    }

    /**
     * 时间更新
     */
    onTimeUpdate() {
        const currentTime = this.audio.currentTime;
        const duration = this.audio.duration;
        this.updateProgress(currentTime, duration);
    }

    /**
     * 错误处理
     */
    onError(e) {
        console.error('音频错误:', e);
        this.showError('音频加载失败');
    }

    // UI 更新方法
    updateUI() {
        const track = this.playlist[this.currentIndex];
        const titleEl = document.getElementById('player-title');
        const artistEl = document.getElementById('player-artist');
        
        if (titleEl) titleEl.textContent = track.title;
        if (artistEl) artistEl.textContent = track.artist || '未知艺术家';
    }

    updatePlayButton() {
        const btn = document.getElementById('player-play-btn');
        if (btn) {
            btn.textContent = this.isPlaying ? '⏸ 暂停' : '▶ 播放';
        }
    }

    updateLoopButton() {
        const btn = document.getElementById('player-loop-btn');
        if (btn) {
            btn.textContent = this.isLooping ? '🔁 循环开' : '🔂 循环关';
            btn.style.opacity = this.isLooping ? '1' : '0.5';
        }
    }

    updateProgress(current, total) {
        const progressEl = document.getElementById('player-progress');
        const currentTimeEl = document.getElementById('player-current-time');
        
        if (progressEl && total) {
            const percent = (current / total) * 100;
            progressEl.style.width = `${percent}%`;
        }
        
        if (currentTimeEl) {
            currentTimeEl.textContent = this.formatTime(current);
        }
    }

    updateDurationDisplay(duration) {
        const totalTimeEl = document.getElementById('player-total-time');
        if (totalTimeEl) {
            totalTimeEl.textContent = this.formatTime(duration);
        }
    }

    formatTime(seconds) {
        if (isNaN(seconds)) return '0:00';
        const mins = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60);
        return `${mins}:${secs.toString().padStart(2, '0')}`;
    }

    showError(message) {
        const errorEl = document.getElementById('player-error');
        if (errorEl) {
            errorEl.textContent = message;
            errorEl.style.display = 'block';
            setTimeout(() => {
                errorEl.style.display = 'none';
            }, 3000);
        }
    }
}

// 导出
if (typeof module !== 'undefined' && module.exports) {
    module.exports = MusicPlayer;
}

// 默认播放列表
const defaultPlaylist = [
    {
        title: "402",
        artist: "402 小队",
        url: "/assets/music/402.mp3"
    }
];

// 全局播放器实例
let player = null;

// 初始化
function initPlayer() {
    player = new MusicPlayer();
    player.loadPlaylist(defaultPlaylist);
    
    // 绑定事件
    const playBtn = document.getElementById('player-play-btn');
    const prevBtn = document.getElementById('player-prev-btn');
    const nextBtn = document.getElementById('player-next-btn');
    const loopBtn = document.getElementById('player-loop-btn');
    const progressBar = document.getElementById('player-progress-bar');
    
    if (playBtn) playBtn.addEventListener('click', () => player.toggle());
    if (prevBtn) prevBtn.addEventListener('click', () => player.prev());
    if (nextBtn) nextBtn.addEventListener('click', () => player.next());
    if (loopBtn) loopBtn.addEventListener('click', () => player.toggleLoop());
    
    if (progressBar) {
        progressBar.addEventListener('click', (e) => {
            const rect = progressBar.getBoundingClientRect();
            const percent = (e.clientX - rect.left) / rect.width;
            if (player.audio.duration) {
                player.seek(percent * player.audio.duration);
            }
        });
    }
    
    // 自动播放首曲
    if (defaultPlaylist.length > 0) {
        player.play();
    }
}

// DOM 加载完成后初始化
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPlayer);
} else {
    initPlayer();
}
