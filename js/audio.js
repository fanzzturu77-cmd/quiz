// Web Audio API Synthesizer & Audio Asset Manager
class SoundController {
    constructor() {
        this.ctx = null;
        this.enabled = true;
        this.shouldPlayBgMusic = false;
        this.isQuizActive = false;

        // Audio assets
        this.bgMusic = new Audio('images/sound/sound.mp3');
        this.bgMusic.loop = true;
        this.bgMusic.volume = 0.45;

        this.yaySound = new Audio('images/sound/yay.mp3');
        this.yaySound.volume = 0.85;

        this._setupAutoplayFallback();
    }

    init() {
        if (!this.ctx) {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (AudioContext) {
                this.ctx = new AudioContext();
            }
        }
        if (this.ctx && this.ctx.state === 'suspended') {
            this.ctx.resume();
        }
    }

    _setupAutoplayFallback() {
        // Fallback for browser autoplay policies on first user interaction
        const triggerPlay = () => {
            // NEVER autoplay if quiz is active!
            if (this.enabled && this.shouldPlayBgMusic && !this.isQuizActive && this.bgMusic && this.bgMusic.paused) {
                this.bgMusic.play().catch(() => {});
            }
            window.removeEventListener('click', triggerPlay);
            window.removeEventListener('touchstart', triggerPlay);
            window.removeEventListener('pointerdown', triggerPlay);
        };
        window.addEventListener('click', triggerPlay, { once: true });
        window.addEventListener('touchstart', triggerPlay, { once: true });
        window.addEventListener('pointerdown', triggerPlay, { once: true });
    }

    playBgMusic() {
        // Strict guard: NEVER play background music if user is in quiz!
        if (this.isQuizActive) {
            this.stopBgMusic();
            return;
        }
        this.shouldPlayBgMusic = true;
        if (!this.enabled || !this.bgMusic) return;

        const promise = this.bgMusic.play();
        if (promise !== undefined) {
            promise.catch(err => {
                // Autoplay blocked; will be triggered on first gesture
            });
        }
    }

    pauseBgMusic() {
        this.shouldPlayBgMusic = false;
        if (this.bgMusic) {
            this.bgMusic.pause();
        }
    }

    stopBgMusic() {
        this.shouldPlayBgMusic = false;
        if (this.bgMusic) {
            this.bgMusic.pause();
            this.bgMusic.currentTime = 0;
        }
    }

    playYay() {
        if (!this.enabled || !this.yaySound) return;
        this.yaySound.currentTime = 0;
        this.yaySound.play().catch(e => console.log('Yay playback error:', e));
    }

    toggle() {
        this.enabled = !this.enabled;
        if (!this.enabled) {
            if (this.bgMusic) this.bgMusic.pause();
            if (this.yaySound) this.yaySound.pause();
        } else {
            if (this.shouldPlayBgMusic && !this.isQuizActive) {
                this.playBgMusic();
            }
        }
        return this.enabled;
    }

    playClick() {
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, this.ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(880, this.ctx.currentTime + 0.05);
        gain.gain.setValueAtTime(0.15, this.ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.05);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start();
        osc.stop(this.ctx.currentTime + 0.05);
    }

    playCorrect() {
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const notes = [523.25, 659.25, 783.99, 1046.50];
        notes.forEach((freq, idx) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, now + idx * 0.08);
            gain.gain.setValueAtTime(0.2, now + idx * 0.08);
            gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.08 + 0.25);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + idx * 0.08);
            osc.stop(now + idx * 0.08 + 0.25);
        });
    }

    playWrong() {
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.exponentialRampToValueAtTime(110, now + 0.2);
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.2);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.2);
    }

    playCoin() {
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc1 = this.ctx.createOscillator();
        const osc2 = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc1.type = 'sine';
        osc2.type = 'sine';
        osc1.frequency.setValueAtTime(987.77, now);
        osc2.frequency.setValueAtTime(1318.51, now + 0.08);
        gain.gain.setValueAtTime(0.18, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
        osc1.connect(gain);
        osc2.connect(gain);
        gain.connect(this.ctx.destination);
        osc1.start(now);
        osc1.stop(now + 0.08);
        osc2.start(now + 0.08);
        osc2.stop(now + 0.35);
    }

    playFanfare() {
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const chord = [523.25, 659.25, 783.99, 1046.50];
        chord.forEach((freq) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, now);
            gain.gain.setValueAtTime(0.15, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.7);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now);
            osc.stop(now + 0.7);
        });
    }
}
