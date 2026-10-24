// Main Application Logic for Demokrasi Challenge
// 8 Levels x 10 Questions = 80 Questions with Realtime Data & Auto-Advance
// ALL DATA IS REALTIME — backed by localStorage, starts from zero for new users

document.addEventListener('DOMContentLoaded', () => {
    // Sound Controller Instance
    const sounds = new SoundController();

    // State
    const state = {
        coins: 0,
        level: 1,
        currentLevelId: 1, // Active level (1 to 8)
        playerName: '',
        playerAbsen: '',
        currentQuestionIndex: 0,
        score: 0,
        correctCount: 0,
        streak: 0,
        maxStreak: 0,
        lives: 3,
        maxLives: 3,
        timerSeconds: 30, // 30 seconds per question
        totalTimePerQuestion: 30,
        timerInterval: null,
        autoAdvanceTimeout: null,
        soundEnabled: true,
        quizActive: false,
        selectedOptionIndex: null,
        answered: false,
        totalLearningSeconds: 0
    };

    // DOM Elements
    const elements = {
        appContainer: document.getElementById('appContainer'),
        
        // Audio & Top Controls
        btnSoundToggle: document.getElementById('btnSoundToggle'),
        soundIcon: document.getElementById('soundIcon'),
        btnOpenOnboarding: document.getElementById('btnOpenOnboarding'),
        
        // HUD
        hudPlayerName: document.getElementById('hudPlayerName'),
        userCoins: document.getElementById('userCoins'),
        levelProgressBar: document.querySelector('.level-progress-bar'),
        levelSubTag: document.querySelector('.level-sub-tag'),
        
        // Player Input
        inputPlayerName: document.getElementById('inputPlayerName'),
        inputPlayerAbsen: document.getElementById('inputPlayerAbsen'),
        playerIdentityBox: document.getElementById('playerIdentityBox'),
        greetingMessage: document.getElementById('greetingMessage'),
        
        // Home Action Buttons
        btnStartGame: document.getElementById('btnStartGame'),
        btnSelectLevel: document.getElementById('btnSelectLevel'),
        btnInstructions: document.getElementById('btnInstructions'),
        btnLeaderboard: document.getElementById('btnLeaderboard'),
        badgesGrid: document.getElementById('badgesGrid'),
        badgesCountChip: document.querySelector('.badges-count-chip'),
        
        // Today's Fun cards
        funNumberTopic: document.querySelector('#cardTopicStats .fun-number'),
        funNumberTime: document.querySelector('#cardTimeStats .fun-number'),
        
        // Quiz Screen Elements
        quizOverlay: document.getElementById('quizOverlay'),
        btnExitQuiz: document.getElementById('btnExitQuiz'),
        quizTimerVal: document.getElementById('quizTimerVal'),
        skyLivesPill: document.getElementById('skyLivesPill'),
        heart1: document.getElementById('heart1'),
        heart2: document.getElementById('heart2'),
        heart3: document.getElementById('heart3'),
        quizTopicPill: document.getElementById('quizTopicPill'),
        quizQuestionTitle: document.getElementById('quizQuestionTitle'),
        quizStepText: document.getElementById('quizStepText'),
        quizDiffPill: document.getElementById('quizDiffPill'),
        quizStreakPill: document.getElementById('quizStreakPill'),
        quizStreakCount: document.getElementById('quizStreakCount'),
        quizOptionsList: document.getElementById('quizOptionsList'),
        quizFeedbackBox: document.getElementById('quizFeedbackBox'),
        feedbackBadge: document.getElementById('feedbackBadge'),
        feedbackText: document.getElementById('feedbackText'),
        btnSubmitAnswer: document.getElementById('btnSubmitAnswer'),
        
        // Results Elements
        resultOverlay: document.getElementById('resultOverlay'),
        resultHeadlineBold: document.getElementById('resultHeadlineBold'),
        resultTopRankVal: document.getElementById('resultTopRankVal'),
        resultBestStreakVal: document.getElementById('resultBestStreakVal'),
        resultXpEarnedVal: document.getElementById('resultXpEarnedVal'),
        resultLearningTimeVal: document.getElementById('resultLearningTimeVal'),
        resultStudentName: document.getElementById('resultStudentName'),
        resultStudentAbsen: document.getElementById('resultStudentAbsen'),
        resultJourneyDate: document.getElementById('resultJourneyDate'),
        resultBadgeEarnedBox: document.getElementById('resultBadgeEarnedBox'),
        resultBadgeImg: document.getElementById('resultBadgeImg'),
        resultBadgeLevelChip: document.getElementById('resultBadgeLevelChip'),
        resultBadgeStatusTitle: document.getElementById('resultBadgeStatusTitle'),
        resultBadgeScorePill: document.getElementById('resultBadgeScorePill'),
        btnResultNextLevel: document.getElementById('btnResultNextLevel'),
        btnResultNextLevelText: document.getElementById('btnResultNextLevelText'),
        btnShareResults: document.getElementById('btnShareResults'),
        btnResultReplay: document.getElementById('btnResultReplay'),
        btnResultChooseLevel: document.getElementById('btnResultChooseLevel'),
        btnResultClose: document.getElementById('btnResultClose'),
        
        // Fullscreen White Onboarding Welcome Screen
        welcomeOnboardingScreen: document.getElementById('welcomeOnboardingScreen'),
        btnEnterApp: document.getElementById('btnEnterApp'),
        btnSkipWelcome: document.getElementById('btnSkipWelcome'),
        welcomeMascotImg: document.getElementById('welcomeMascotImg'),
        
        // Modals
        levelSelectModal: document.getElementById('levelSelectModal'),
        btnCloseLevelSelect: document.getElementById('btnCloseLevelSelect'),
        btnLevelSelectClose: document.getElementById('btnLevelSelectClose'),
        levelCardsGrid: document.getElementById('levelCardsGrid'),
        
        instructionModal: document.getElementById('instructionModal'),
        btnCloseInstructions: document.getElementById('btnCloseInstructions'),
        btnStartFromGuide: document.getElementById('btnStartFromGuide'),
        
        leaderboardModal: document.getElementById('leaderboardModal'),
        btnCloseLeaderboard: document.getElementById('btnCloseLeaderboard'),
        btnLeaderboardClose: document.getElementById('btnLeaderboardClose'),
        leaderboardList: document.getElementById('leaderboardList'),
        
        badgeModal: document.getElementById('badgeModal'),
        btnCloseBadgeModal: document.getElementById('btnCloseBadgeModal'),
        btnBadgeModalDone: document.getElementById('btnBadgeModalDone'),
        badgeModalContent: document.getElementById('badgeModalContent'),
        
        // Toast & Confetti
        toastNotification: document.getElementById('toastNotification'),
        toastMessage: document.getElementById('toastMessage'),
        confettiCanvas: document.getElementById('confettiCanvas')
    };

    // =========================================================================
    // 1. Toast Notification Helper
    // =========================================================================
    let toastTimeout = null;
    function showToast(msg) {
        if (!elements.toastNotification) return;
        elements.toastMessage.textContent = msg;
        elements.toastNotification.classList.remove('hidden');
        clearTimeout(toastTimeout);
        toastTimeout = setTimeout(() => {
            elements.toastNotification.classList.add('hidden');
        }, 2800);
    }

    // =========================================================================
    // 2. Text-to-Speech Audio Helper
    // =========================================================================
    function speakText(text) {
        if (!state.soundEnabled) return;
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'id-ID';
            utterance.rate = 1.0;
            window.speechSynthesis.speak(utterance);
        } else {
            sounds.playClick();
        }
    }

    // =========================================================================
    // 3. REALTIME Player Identity & Stats Management
    // =========================================================================
    function refreshHUDFromRealtime() {
        const stats = realtimeData.getPlayerStats();
        
        // Update coins display
        state.coins = stats.coins;
        elements.userCoins.textContent = stats.coins;
        
        // Update level
        state.level = stats.level;
        if (elements.levelSubTag) {
            elements.levelSubTag.textContent = `Lvl ${stats.level}`;
        }
        if (elements.levelProgressBar) {
            const unlockedBadges = realtimeData.getUnlockedBadgeCount();
            const progress = Math.min(100, (unlockedBadges / 8) * 100);
            elements.levelProgressBar.style.width = `${progress}%`;
        }
        
        // Update badge count chip
        const unlockedCount = realtimeData.getUnlockedBadgeCount();
        if (elements.badgesCountChip) {
            elements.badgesCountChip.textContent = `${unlockedCount}/8 Lencana`;
        }
        
        // Update Today's Fun cards with real data
        if (elements.funNumberTopic) {
            elements.funNumberTopic.textContent = stats.totalGames > 0 
                ? `${stats.totalCorrect} Benar` 
                : '0 Benar';
        }
        if (elements.funNumberTime) {
            if (stats.totalLearningSeconds > 0) {
                const mins = Math.floor(stats.totalLearningSeconds / 60);
                const secs = stats.totalLearningSeconds % 60;
                elements.funNumberTime.textContent = mins > 0 ? `${mins}m ${secs}d` : `${secs} Detik`;
            } else {
                elements.funNumberTime.textContent = '0 Detik';
            }
        }
    }

    function loadSavedPlayer() {
        const savedName = localStorage.getItem('demokrasi_player_name');
        const savedAbsen = localStorage.getItem('demokrasi_player_absen');

        if (savedName) {
            state.playerName = savedName;
            elements.inputPlayerName.value = savedName;
            elements.hudPlayerName.textContent = savedName;
        } else {
            elements.hudPlayerName.textContent = 'Pemain Baru';
        }
        if (savedAbsen) {
            state.playerAbsen = savedAbsen;
            elements.inputPlayerAbsen.value = savedAbsen;
        }

        refreshHUDFromRealtime();
        updateGreetingMessage();
    }

    function updateGreetingMessage() {
        const nameVal = elements.inputPlayerName.value.trim();
        const absenVal = elements.inputPlayerAbsen.value.trim();
        const stats = realtimeData.getPlayerStats();
        const unlockedCount = realtimeData.getUnlockedBadgeCount();

        if (nameVal && absenVal) {
            if (stats.totalGames > 0) {
                elements.greetingMessage.innerHTML = `Selamat datang kembali, <strong>${nameVal}</strong> (Absen #${absenVal})! ${unlockedCount}/8 Lencana terkoleksi 🏅`;
            } else {
                elements.greetingMessage.innerHTML = `Halo, <strong>${nameVal}</strong> (Absen #${absenVal})! Siap menaklukkan 8 level kebangsaan! 🇮🇩✨`;
            }
        } else if (nameVal) {
            elements.greetingMessage.innerHTML = `Halo, <strong>${nameVal}</strong>! Jangan lupa masukkan nomor absenmu! 🔢`;
        } else {
            elements.greetingMessage.textContent = 'Isi nama dan nomor absen untuk memulai petualangan kuis! 📝';
        }
    }

    elements.inputPlayerName.addEventListener('input', () => {
        const nameVal = elements.inputPlayerName.value.trim();
        elements.hudPlayerName.textContent = nameVal || 'Pemain Baru';
        updateGreetingMessage();
    });

    elements.inputPlayerAbsen.addEventListener('input', () => {
        updateGreetingMessage();
    });

    function validateAndSavePlayer() {
        const name = elements.inputPlayerName.value.trim();
        const absen = elements.inputPlayerAbsen.value.trim();

        if (!name) {
            sounds.playWrong();
            elements.playerIdentityBox.classList.add('shake-error');
            elements.inputPlayerName.focus();
            showToast('⚠️ Silakan isi Nama Pemain / Siswa terlebih dahulu!');
            setTimeout(() => elements.playerIdentityBox.classList.remove('shake-error'), 500);
            return false;
        }

        if (!absen) {
            sounds.playWrong();
            elements.playerIdentityBox.classList.add('shake-error');
            elements.inputPlayerAbsen.focus();
            showToast('⚠️ Silakan masukkan Nomor Absenmu!');
            setTimeout(() => elements.playerIdentityBox.classList.remove('shake-error'), 500);
            return false;
        }

        state.playerName = name;
        state.playerAbsen = absen;

        localStorage.setItem('demokrasi_player_name', name);
        localStorage.setItem('demokrasi_player_absen', absen);

        elements.hudPlayerName.textContent = name;
        return true;
    }

    // =========================================================================
    // 4. Fullscreen White Onboarding Welcome Screen
    // =========================================================================
    function openWelcomeScreen() {
        sounds.playClick();
        if (!elements.welcomeOnboardingScreen) return;
        elements.welcomeOnboardingScreen.classList.remove('hidden');

        const penguin = document.getElementById('welcomePenguinActor');
        const words = document.getElementById('welcomeWordsActor');
        if (penguin && words) {
            penguin.style.animation = 'none';
            words.style.animation = 'none';
            void penguin.offsetWidth;
            void words.offsetWidth;
            penguin.style.animation = '';
            words.style.animation = '';
        }
    }

    function closeWelcomeScreen() {
        sounds.playClick();
        if (elements.welcomeOnboardingScreen) {
            elements.welcomeOnboardingScreen.classList.add('hidden');
        }
        sounds.isQuizActive = false;
        sounds.playBgMusic();
    }

    if (elements.btnEnterApp) elements.btnEnterApp.addEventListener('click', closeWelcomeScreen);
    if (elements.btnSkipWelcome) elements.btnSkipWelcome.addEventListener('click', closeWelcomeScreen);
    if (elements.btnOpenOnboarding) elements.btnOpenOnboarding.addEventListener('click', openWelcomeScreen);

    // =========================================================================
    // 5. Level Selection Modal (8 Levels & Badges Progression)
    // =========================================================================
    function openLevelSelectModal() {
        if (!validateAndSavePlayer()) return;
        sounds.playClick();
        renderLevelCards();
        elements.levelSelectModal.classList.remove('hidden');
    }

    function closeLevelSelectModal() {
        sounds.playClick();
        elements.levelSelectModal.classList.add('hidden');
    }

    function renderLevelCards() {
        if (!elements.levelCardsGrid) return;
        elements.levelCardsGrid.innerHTML = '';

        const progress = realtimeData.getLevelProgress();

        QUIZ_DATA.levels.forEach((lvl) => {
            const p = progress[lvl.id] || { unlocked: lvl.id === 1, passed: false, bestScore: 0 };
            const card = document.createElement('div');
            card.className = `level-card ${p.passed ? 'passed' : (p.unlocked ? 'unlocked' : 'locked')}`;
            
            let statusBadgeHtml = '';
            let actionBtnText = 'MAIN ▶';
            
            if (p.passed) {
                statusBadgeHtml = `<span class="level-card-status-badge status-badge-passed">Lulus ⭐ (${p.bestScore}/100)</span>`;
                actionBtnText = 'MAIN LAGI 🔄';
            } else if (p.unlocked) {
                if (p.attempts > 0) {
                    statusBadgeHtml = `<span class="level-card-status-badge status-badge-unlocked">Skor: ${p.bestScore}/100 (Min. 80)</span>`;
                    actionBtnText = 'ULANGI 🔄';
                } else {
                    statusBadgeHtml = `<span class="level-card-status-badge status-badge-unlocked">Terbuka 🔓</span>`;
                    actionBtnText = 'MULAI ▶';
                }
            } else {
                statusBadgeHtml = `<span class="level-card-status-badge status-badge-locked">Terkunci 🔒</span>`;
                actionBtnText = 'TERKUNCI';
            }

            card.innerHTML = `
                <div class="level-card-thumb-wrap">
                    <img src="${lvl.badgeImage}" alt="${lvl.badgeName}" class="level-card-thumb">
                    ${!p.unlocked ? '<span class="level-lock-overlay-icon">🔒</span>' : ''}
                </div>
                <div class="level-card-main">
                    <div class="level-card-header">
                        <span class="level-card-num">Level ${lvl.id}</span>
                        ${statusBadgeHtml}
                    </div>
                    <div class="level-card-title">${lvl.shortTitle}</div>
                    <div class="level-card-focus">${lvl.focus}</div>
                </div>
                <button type="button" class="level-card-action-btn" ${!p.unlocked ? 'disabled' : ''}>
                    ${actionBtnText}
                </button>
            `;

            if (p.unlocked) {
                card.addEventListener('click', () => {
                    closeLevelSelectModal();
                    startLevelQuiz(lvl.id);
                });
            } else {
                card.addEventListener('click', () => {
                    sounds.playWrong();
                    showToast(`🔒 Level ${lvl.id} masih terkunci! Selesaikan Level ${lvl.id - 1} dengan minimal 80 poin.`);
                });
            }

            elements.levelCardsGrid.appendChild(card);
        });
    }

    if (elements.btnSelectLevel) {
        elements.btnSelectLevel.addEventListener('click', openLevelSelectModal);
    }
    if (elements.btnCloseLevelSelect) {
        elements.btnCloseLevelSelect.addEventListener('click', closeLevelSelectModal);
    }
    if (elements.btnLevelSelectClose) {
        elements.btnLevelSelectClose.addEventListener('click', closeLevelSelectModal);
    }

    // =========================================================================
    // 6. Render Badges (8 Level Badges in Dashboard)
    // =========================================================================
    function renderBadges() {
        if (!elements.badgesGrid) return;
        elements.badgesGrid.innerHTML = '';

        const badges = realtimeData.getBadges();
        const unlockedCount = badges.filter(b => b.unlocked).length;

        if (elements.badgesCountChip) {
            elements.badgesCountChip.textContent = `${unlockedCount}/8 Lencana`;
        }

        badges.forEach((b) => {
            const item = document.createElement('div');
            item.className = `badge-item ${b.unlocked ? 'unlocked' : 'locked'}`;
            item.title = `${b.name} (${b.alias})`;
            item.innerHTML = `
                <div class="badge-avatar-wrap">
                    <img src="${b.image}" alt="${b.name}" class="badge-img" loading="lazy">
                </div>
                <div class="badge-title">${b.alias}</div>
                <div class="badge-count">${b.progress}</div>
            `;
            item.addEventListener('click', () => {
                sounds.playClick();
                showBadgeDetail(b);
            });
            elements.badgesGrid.appendChild(item);
        });
    }

    function showBadgeDetail(badge) {
        if (!elements.badgeModalContent) return;
        const progress = realtimeData.getLevelProgress();
        const lvlProg = progress[badge.id] || { unlocked: badge.id === 1, passed: false, bestScore: 0 };

        let actionButtonHtml = '';
        if (lvlProg.unlocked) {
            actionButtonHtml = `
                <button type="button" class="sheet-primary-btn" id="btnPlayFromBadgeModal" style="margin-top: 14px;">
                    ${lvlProg.passed ? 'Mainkan Lagi Level ' + badge.id + ' ▶' : 'Mulai Level ' + badge.id + ' Sekarang ▶'}
                </button>
            `;
        }

        elements.badgeModalContent.innerHTML = `
            <img src="${badge.image}" alt="${badge.name}" class="badge-modal-img">
            <h4 class="badge-modal-title">${badge.name}</h4>
            <div class="badge-modal-alias">Badge Level ${badge.id}: ${badge.alias}</div>
            <p class="badge-modal-desc">${badge.desc}</p>
            <div class="badge-modal-progress">
                <div class="badge-modal-bar" style="width: ${badge.unlocked ? '100%' : (lvlProg.unlocked ? '50%' : '15%')};"></div>
            </div>
            <div style="font-size: 0.8rem; font-weight: 700; color: #475569; margin-top: 6px;">
                ${badge.unlocked ? '✅ Lencana Diraih (Lulus)' : (lvlProg.unlocked ? '🔓 Level Terbuka (Belum Lulus)' : '🔒 Masih Terkunci')}
            </div>
            <div style="margin-top: 6px; font-size: 0.75rem; color: #64748b;">
                Syarat: Minimal 80 Poin di Level ${badge.id}
            </div>
            ${actionButtonHtml}
        `;

        const playBtn = document.getElementById('btnPlayFromBadgeModal');
        if (playBtn) {
            playBtn.addEventListener('click', () => {
                elements.badgeModal.classList.add('hidden');
                startLevelQuiz(badge.id);
            });
        }

        elements.badgeModal.classList.remove('hidden');
    }

    // =========================================================================
    // 7. Leaderboard (REALTIME from localStorage)
    // =========================================================================
    function renderLeaderboard() {
        if (!elements.leaderboardList) return;
        elements.leaderboardList.innerHTML = '';

        const entries = realtimeData.getLeaderboard();

        if (entries.length === 0) {
            elements.leaderboardList.innerHTML = `
                <div class="leaderboard-empty-state">
                    <div class="empty-icon">🏆</div>
                    <h4 class="empty-title">Belum Ada Peringkat</h4>
                    <p class="empty-desc">Papan skor masih kosong! Mainkan kuis dan raih nilai tertinggi!</p>
                </div>
            `;
            return;
        }

        const currentPlayerKey = `${state.playerName.toLowerCase().trim()}_${state.playerAbsen}`;
        const rankAvatars = ['👑', '⭐', '🔥'];
        const defaultAvatars = ['🎯', '✨', '🌿', '💎', '🌟', '🎓', '⚡'];

        entries.forEach((entry, idx) => {
            const rank = idx + 1;
            const isCurrentUser = entry.key === currentPlayerKey;
            const avatar = rank <= 3 ? rankAvatars[rank - 1] : defaultAvatars[idx % defaultAvatars.length];

            const row = document.createElement('div');
            row.className = `leader-item ${isCurrentUser ? 'is-user' : ''}`;
            row.innerHTML = `
                <div class="leader-rank">#${rank}</div>
                <div class="leader-avatar">${avatar}</div>
                <div class="leader-name-wrap">
                    <div class="leader-name">${entry.name}${isCurrentUser ? ' (Kamu)' : ''}</div>
                    <div class="leader-badges">No. Absen: ${entry.absen || '-'} &bull; ${entry.gamesPlayed}x Main</div>
                </div>
                <div class="leader-score">${entry.score} Poin</div>
            `;
            elements.leaderboardList.appendChild(row);
        });
    }

    // =========================================================================
    // 8. Interactive Quiz Engine (30s Timer + Auto-Advance)
    // =========================================================================
    function updateHeartsDisplay() {
        const hearts = [elements.heart1, elements.heart2, elements.heart3];
        hearts.forEach((h, idx) => {
            if (idx < state.lives) {
                h.textContent = '❤️';
                h.className = 'heart-icon active';
            } else {
                h.textContent = '🤍';
                h.className = 'heart-icon inactive';
            }
        });
    }

    function formatTime(totalSeconds) {
        const mins = Math.floor(totalSeconds / 60);
        const secs = totalSeconds % 60;
        return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    }

    // Quick start button on hero: starts first non-passed unlocked level or opens level selector
    function handleHeroPlayClick() {
        if (!validateAndSavePlayer()) return;
        const progress = realtimeData.getLevelProgress();
        
        // Find first unlocked level that hasn't been passed yet
        let targetLevel = 1;
        for (let i = 1; i <= 8; i++) {
            if (progress[i]?.unlocked && !progress[i]?.passed) {
                targetLevel = i;
                break;
            }
            if (progress[i]?.unlocked) {
                targetLevel = i;
            }
        }
        
        startLevelQuiz(targetLevel);
    }

    function startLevelQuiz(levelId) {
        if (!validateAndSavePlayer()) return;

        state.currentLevelId = Number(levelId) || 1;
        sounds.playClick();
        
        // Stop background music completely during quiz gameplay
        sounds.isQuizActive = true;
        sounds.stopBgMusic();

        state.quizActive = true;
        state.currentQuestionIndex = 0;
        state.score = 0;
        state.correctCount = 0;
        state.streak = 0;
        state.maxStreak = 0;
        state.lives = 3;
        state.selectedOptionIndex = null;
        state.answered = false;
        state.totalLearningSeconds = 0;

        clearTimeout(state.autoAdvanceTimeout);
        clearInterval(state.timerInterval);

        updateHeartsDisplay();

        elements.quizStreakPill.classList.add('hidden');
        elements.quizOverlay.classList.add('active');
        elements.instructionModal.classList.add('hidden');
        elements.levelSelectModal.classList.add('hidden');
        elements.resultOverlay.classList.add('hidden');

        loadQuestion(state.currentQuestionIndex);
    }

    function exitQuiz() {
        sounds.playClick();
        if (confirm('Yakin ingin keluar dari kuis? Skor sesi ini tidak akan tersimpan.')) {
            clearInterval(state.timerInterval);
            clearTimeout(state.autoAdvanceTimeout);
            state.quizActive = false;
            sounds.isQuizActive = false;
            elements.quizOverlay.classList.remove('active');
            sounds.playBgMusic();
        }
    }

    function loadQuestion(index) {
        clearInterval(state.timerInterval);
        clearTimeout(state.autoAdvanceTimeout);

        sounds.isQuizActive = true;
        sounds.stopBgMusic();
        state.answered = false;
        state.selectedOptionIndex = null;

        elements.quizFeedbackBox.classList.add('hidden');
        elements.quizFeedbackBox.className = 'sky-feedback-bubble hidden';

        // Reset submit button state
        elements.btnSubmitAnswer.textContent = 'KIRIM JAWABAN';
        elements.btnSubmitAnswer.disabled = true;

        const currentLevel = QUIZ_DATA.getLevel(state.currentLevelId);
        const questionsList = currentLevel.questions;
        const q = questionsList[index];
        const total = questionsList.length; // 10

        // Topic & Step Chip
        elements.quizTopicPill.textContent = currentLevel.name;
        elements.quizStepText.textContent = `Soal ${index + 1} / ${total}`;
        elements.quizDiffPill.textContent = q.difficulty || currentLevel.difficulty;

        // Format Question
        elements.quizQuestionTitle.innerHTML = q.question;

        // Render Options (A, B, C, D)
        elements.quizOptionsList.innerHTML = '';
        const letters = ['A', 'B', 'C', 'D'];

        q.options.forEach((optText, optIdx) => {
            const btn = document.createElement('div');
            btn.className = 'sky-option-btn';
            btn.dataset.index = optIdx;
            btn.innerHTML = `
                <div class="sky-option-letter-circle">${letters[optIdx]}</div>
                <div class="sky-option-text">${optText}</div>
                <button type="button" class="sky-option-speaker" title="Dengarkan Suara" aria-label="Dengarkan">🔊</button>
            `;

            btn.addEventListener('click', (e) => {
                if (e.target.classList.contains('sky-option-speaker')) {
                    e.stopPropagation();
                    speakText(optText);
                    return;
                }
                if (state.answered) return;
                selectOption(optIdx);
            });

            elements.quizOptionsList.appendChild(btn);
        });

        // Setup 30-Second Timer per question
        state.timerSeconds = 30;
        elements.quizTimerVal.textContent = formatTime(state.timerSeconds);

        state.timerInterval = setInterval(() => {
            state.timerSeconds--;
            state.totalLearningSeconds++;
            elements.quizTimerVal.textContent = formatTime(state.timerSeconds);

            if (state.timerSeconds <= 0) {
                clearInterval(state.timerInterval);
                handleTimeOut(q);
            }
        }, 1000);
    }

    function selectOption(index) {
        if (state.answered) return;
        sounds.playClick();
        state.selectedOptionIndex = index;

        const allButtons = elements.quizOptionsList.querySelectorAll('.sky-option-btn');
        allButtons.forEach((b, idx) => {
            b.classList.toggle('selected', idx === index);
        });

        elements.btnSubmitAnswer.disabled = false;
    }

    // Submit Answer Handler
    elements.btnSubmitAnswer.addEventListener('click', () => {
        if (!state.answered) {
            submitAnswer();
        }
    });

    function submitAnswer() {
        if (state.selectedOptionIndex === null || state.answered) return;
        state.answered = true;
        clearInterval(state.timerInterval);

        const currentLevel = QUIZ_DATA.getLevel(state.currentLevelId);
        const q = currentLevel.questions[state.currentQuestionIndex];
        const allButtons = elements.quizOptionsList.querySelectorAll('.sky-option-btn');
        const selectedBtn = allButtons[state.selectedOptionIndex];

        // Disable all options clicks
        allButtons.forEach(b => b.classList.add('disabled'));

        const isCorrect = state.selectedOptionIndex === q.correct;

        if (isCorrect) {
            sounds.playCorrect();
            selectedBtn.classList.add('correct');
            state.correctCount++;
            state.streak++;
            if (state.streak > state.maxStreak) {
                state.maxStreak = state.streak;
            }

            if (state.streak >= 2) {
                elements.quizStreakCount.textContent = state.streak;
                elements.quizStreakPill.classList.remove('hidden');
            }

            // Exactly 10 points per question (10 x 10 = 100 max points per level)
            state.score += 10;

            elements.feedbackBadge.textContent = '🎉 Jawaban Tepat! (+10 Poin)';
            elements.quizFeedbackBox.classList.remove('hidden');
            elements.quizFeedbackBox.className = 'sky-feedback-bubble correct-bubble';
        } else {
            sounds.playWrong();
            selectedBtn.classList.add('wrong');
            state.streak = 0;
            elements.quizStreakPill.classList.add('hidden');

            // Highlight the correct one
            allButtons[q.correct].classList.add('correct');

            // Deduct 1 life
            state.lives--;
            updateHeartsDisplay();

            elements.feedbackBadge.textContent = '💡 Jawaban Belum Tepat (-1 Nyawa)';
            elements.quizFeedbackBox.classList.remove('hidden');
            elements.quizFeedbackBox.className = 'sky-feedback-bubble wrong-bubble';
        }

        elements.feedbackText.textContent = q.explanation;
        elements.btnSubmitAnswer.disabled = true;
        elements.btnSubmitAnswer.innerHTML = '<span class="auto-advance-pulse">⏩ Otomatis lanjut ke soal berikutnya...</span>';

        // AUTO-ADVANCE: smoothly advance to next question after 1.8 seconds!
        clearTimeout(state.autoAdvanceTimeout);
        state.autoAdvanceTimeout = setTimeout(() => {
            if (!state.quizActive) return;
            nextQuestion();
        }, 1800);
    }

    function handleTimeOut(question) {
        if (state.answered) return;
        state.answered = true;
        sounds.playWrong();

        state.streak = 0;
        elements.quizStreakPill.classList.add('hidden');

        const allButtons = elements.quizOptionsList.querySelectorAll('.sky-option-btn');
        allButtons.forEach(b => b.classList.add('disabled'));
        allButtons[question.correct].classList.add('correct');

        // Deduct 1 life
        state.lives--;
        updateHeartsDisplay();

        elements.feedbackBadge.textContent = '⏰ Waktu Habis! (-1 Nyawa)';
        elements.feedbackText.textContent = question.explanation;
        elements.quizFeedbackBox.classList.remove('hidden');
        elements.quizFeedbackBox.className = 'sky-feedback-bubble wrong-bubble';

        elements.btnSubmitAnswer.disabled = true;
        elements.btnSubmitAnswer.innerHTML = '<span class="auto-advance-pulse">⏩ Waktu habis, otomatis lanjut...</span>';

        // Auto-advance after 1.8 seconds on timeout
        clearTimeout(state.autoAdvanceTimeout);
        state.autoAdvanceTimeout = setTimeout(() => {
            if (!state.quizActive) return;
            nextQuestion();
        }, 1800);
    }

    function nextQuestion() {
        clearTimeout(state.autoAdvanceTimeout);
        const currentLevel = QUIZ_DATA.getLevel(state.currentLevelId);
        const total = currentLevel.questions.length;

        // If out of lives or finished all 10 questions, transition to finishQuiz
        if (state.lives <= 0 || state.currentQuestionIndex >= total - 1) {
            finishQuiz();
            return;
        }

        state.currentQuestionIndex++;
        loadQuestion(state.currentQuestionIndex);
    }

    // =========================================================================
    // 9. Quiz Results (REALTIME — Level Badge Progression)
    // =========================================================================
    function finishQuiz() {
        clearInterval(state.timerInterval);
        clearTimeout(state.autoAdvanceTimeout);
        state.quizActive = false;
        sounds.isQuizActive = false;
        sounds.stopBgMusic();

        // Celebration sounds
        sounds.playYay();
        sounds.playCoin();

        elements.quizOverlay.classList.remove('active');

        const currentLevel = QUIZ_DATA.getLevel(state.currentLevelId);

        // --- RECORD GAME RESULT IN REALTIME SYSTEM ---
        const gameResult = {
            score: state.score,
            correctCount: state.correctCount,
            totalQuestions: currentLevel.questions.length, // 10
            maxStreak: state.maxStreak,
            learningSeconds: state.totalLearningSeconds
        };

        const outcome = realtimeData.recordLevelGameResult(state.currentLevelId, gameResult);

        // Update leaderboard
        realtimeData.updateLeaderboard(
            state.playerName, 
            state.playerAbsen, 
            state.score, 
            state.correctCount, 
            currentLevel.questions.length,
            state.currentLevelId
        );

        // Add to history
        realtimeData.addGameToHistory({
            ...gameResult,
            levelId: state.currentLevelId
        });

        // Current Date in Indonesian format
        const now = new Date();
        const namaBulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"];
        const formattedDate = `${now.getDate()} ${namaBulan[now.getMonth()]} ${now.getFullYear()}`;
        elements.resultJourneyDate.textContent = `Perjalanan Demokrasimu per ${formattedDate}`;

        // Populate Student Identity
        elements.resultStudentName.textContent = state.playerName || 'Pemain Baru';
        elements.resultStudentAbsen.textContent = `No. Absen: ${state.playerAbsen || '-'}`;

        // Top Ranking from leaderboard
        const rankText = realtimeData.getTopRankingPercent(state.playerName, state.playerAbsen);
        elements.resultTopRankVal.textContent = rankText;

        // Headline & Badge Outcome
        elements.resultBadgeImg.src = currentLevel.badgeImage;
        elements.resultBadgeLevelChip.textContent = `Level ${currentLevel.id} — ${currentLevel.shortTitle}`;

        const isPassed = state.score >= 80;

        if (isPassed) {
            elements.resultHeadlineBold.textContent = `Luar Biasa! Kamu Lulus ${currentLevel.shortTitle}! 🎉`;
            elements.resultBadgeStatusTitle.textContent = `🎉 LULUS & MERAIH LENCANA!`;
            elements.resultBadgeStatusTitle.style.color = '#059669';
            elements.resultBadgeScorePill.textContent = `Skor: ${state.score}/100 (${state.correctCount}/10 Benar) • Lencana Tersimpan!`;

            // If there's a next level, show next level button
            if (state.currentLevelId < 8) {
                elements.btnResultNextLevel.classList.remove('hidden');
                elements.btnResultNextLevelText.textContent = `LANJUT KE LEVEL ${state.currentLevelId + 1} ▶`;
            } else {
                elements.btnResultNextLevel.classList.add('hidden');
            }

            launchConfetti();
            showToast(`🏅 Selamat! Kamu mendapatkan Lencana ${currentLevel.badgeName}!`);
        } else {
            elements.resultHeadlineBold.textContent = `Tetap Semangat! Belum Lulus (Minimal 80 Poin) 📚`;
            elements.resultBadgeStatusTitle.textContent = `Belum Lulus (Butuh Min. 80 Poin)`;
            elements.resultBadgeStatusTitle.style.color = '#dc2626';
            elements.resultBadgeScorePill.textContent = `Skor: ${state.score}/100 (${state.correctCount}/10 Benar) • Ulangi level untuk membuka lencana`;

            elements.btnResultNextLevel.classList.add('hidden');
        }

        // Stats boxes
        elements.resultBestStreakVal.textContent = `${state.maxStreak}`;
        elements.resultXpEarnedVal.textContent = `${outcome.gameXP}`;

        const mins = Math.floor(state.totalLearningSeconds / 60);
        const secs = state.totalLearningSeconds % 60;
        elements.resultLearningTimeVal.textContent = mins > 0 ? `${mins}m ${secs}d` : `${secs}d`;

        // Update HUD & Badges
        refreshHUDFromRealtime();
        renderBadges();

        elements.resultOverlay.classList.remove('hidden');
    }

    // =========================================================================
    // 10. Canvas Confetti System
    // =========================================================================
    function launchConfetti() {
        const canvas = elements.confettiCanvas;
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        canvas.width = canvas.parentElement.offsetWidth;
        canvas.height = canvas.parentElement.offsetHeight;

        const particles = [];
        const colors = ['#2ecc71', '#3498db', '#f1c40f', '#e74c3c', '#9b59b6', '#1abc9c', '#f59e0b', '#ffffff'];

        for (let i = 0; i < 90; i++) {
            particles.push({
                x: canvas.width / 2,
                y: canvas.height * 0.35,
                w: Math.random() * 8 + 4,
                h: Math.random() * 6 + 4,
                color: colors[Math.floor(Math.random() * colors.length)],
                vx: (Math.random() - 0.5) * 12,
                vy: (Math.random() - 1) * 10 - 2,
                rotation: Math.random() * 360,
                rSpeed: (Math.random() - 0.5) * 10,
                gravity: 0.28,
                life: 1
            });
        }

        let animFrame;
        function render() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            let aliveCount = 0;

            particles.forEach(p => {
                if (p.life > 0) {
                    aliveCount++;
                    p.x += p.vx;
                    p.y += p.vy;
                    p.vy += p.gravity;
                    p.rotation += p.rSpeed;
                    p.life -= 0.009;

                    ctx.save();
                    ctx.translate(p.x, p.y);
                    ctx.rotate((p.rotation * Math.PI) / 180);
                    ctx.fillStyle = p.color;
                    ctx.globalAlpha = Math.max(0, p.life);
                    ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
                    ctx.restore();
                }
            });

            if (aliveCount > 0) {
                animFrame = requestAnimationFrame(render);
            } else {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                cancelAnimationFrame(animFrame);
            }
        }
        render();
    }

    // =========================================================================
    // 11. Event Listeners & Actions
    // =========================================================================
    
    // Sound Toggle
    if (elements.btnSoundToggle) {
        elements.btnSoundToggle.addEventListener('click', () => {
            state.soundEnabled = sounds.toggle();
            elements.soundIcon.textContent = state.soundEnabled ? '🔊' : '🔇';
            if (state.soundEnabled) sounds.playClick();
        });
    }

    // Quiz Launchers
    elements.btnStartGame.addEventListener('click', handleHeroPlayClick);
    elements.btnStartFromGuide.addEventListener('click', () => {
        elements.instructionModal.classList.add('hidden');
        openLevelSelectModal();
    });
    elements.btnExitQuiz.addEventListener('click', exitQuiz);

    // Modals
    elements.btnInstructions.addEventListener('click', () => {
        sounds.playClick();
        elements.instructionModal.classList.remove('hidden');
    });
    elements.btnCloseInstructions.addEventListener('click', () => {
        sounds.playClick();
        elements.instructionModal.classList.add('hidden');
    });

    elements.btnLeaderboard.addEventListener('click', () => {
        sounds.playClick();
        renderLeaderboard();
        elements.leaderboardModal.classList.remove('hidden');
    });
    elements.btnCloseLeaderboard.addEventListener('click', () => {
        sounds.playClick();
        elements.leaderboardModal.classList.add('hidden');
    });
    elements.btnLeaderboardClose.addEventListener('click', () => {
        sounds.playClick();
        elements.leaderboardModal.classList.add('hidden');
    });

    elements.btnCloseBadgeModal.addEventListener('click', () => {
        sounds.playClick();
        elements.badgeModal.classList.add('hidden');
    });
    elements.btnBadgeModalDone.addEventListener('click', () => {
        sounds.playClick();
        elements.badgeModal.classList.add('hidden');
    });

    // Result Action Buttons
    if (elements.btnResultNextLevel) {
        elements.btnResultNextLevel.addEventListener('click', () => {
            elements.resultOverlay.classList.add('hidden');
            if (state.currentLevelId < 8) {
                startLevelQuiz(state.currentLevelId + 1);
            }
        });
    }

    elements.btnResultReplay.addEventListener('click', () => {
        elements.resultOverlay.classList.add('hidden');
        startLevelQuiz(state.currentLevelId);
    });

    if (elements.btnResultChooseLevel) {
        elements.btnResultChooseLevel.addEventListener('click', () => {
            elements.resultOverlay.classList.add('hidden');
            openLevelSelectModal();
        });
    }

    elements.btnResultClose.addEventListener('click', () => {
        sounds.playClick();
        elements.resultOverlay.classList.add('hidden');
        sounds.isQuizActive = false;
        sounds.playBgMusic();
        refreshHUDFromRealtime();
        renderBadges();
    });

    // SHARE MY RESULTS Button
    elements.btnShareResults.addEventListener('click', () => {
        sounds.playClick();
        const currentLevel = QUIZ_DATA.getLevel(state.currentLevelId);
        const stats = realtimeData.getPlayerStats();
        const shareText = `🌟 PRESTASI DEMOKRASI CHALLENGE 🇮🇩\n\n` +
            `"${elements.resultHeadlineBold.textContent}"\n\n` +
            `👤 Peserta: ${state.playerName}\n` +
            `🔢 No. Absen: ${state.playerAbsen}\n` +
            `🗺️ Level: ${currentLevel.name}\n` +
            `🎯 Nilai: ${state.score}/100 (${state.correctCount}/10 Benar)\n` +
            `📊 Peringkat: ${elements.resultTopRankVal.textContent}\n` +
            `🔥 Streak Terbaik: ${state.maxStreak}\n` +
            `⚡ XP Diraih: ${elements.resultXpEarnedVal.textContent}\n` +
            `🏅 Total Lencana: ${realtimeData.getUnlockedBadgeCount()}/8\n\n` +
            `Bagikan prestasimu dan teruslah belajar untuk masa depan!`;

        if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(shareText).then(() => {
                showToast('📋 Prestasi berhasil disalin ke clipboard!');
            }).catch(() => {
                showToast('Hasil siap dibagikan!');
            });
        } else {
            showToast('📋 Prestasi tercatat sempurna!');
        }
    });

    // Close Modals on click outside backdrop
    [elements.instructionModal, elements.leaderboardModal, elements.badgeModal, elements.levelSelectModal].forEach(modal => {
        if (!modal) return;
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                sounds.playClick();
                modal.classList.add('hidden');
            }
        });
    });

    // Quick start cards on Dashboard
    document.getElementById('cardTopicStats')?.addEventListener('click', () => {
        sounds.playClick();
        openLevelSelectModal();
    });

    document.getElementById('cardTimeStats')?.addEventListener('click', () => {
        sounds.playClick();
        handleHeroPlayClick();
    });

    // Initial Renders & Setup
    loadSavedPlayer();
    renderBadges();
    
    // Autoplay background music
    sounds.playBgMusic();
});
