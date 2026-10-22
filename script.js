document.documentElement.classList.add('js');

const menuToggle = document.querySelector('.menu-toggle');
const primaryNav = document.querySelector('#primary-nav');

if (menuToggle && primaryNav) {
    const isChinese = document.documentElement.lang.toLowerCase().startsWith('zh');
    const openLabel = menuToggle.dataset.openLabel || (isChinese ? '打开导航' : 'Open navigation');
    const closeLabel = menuToggle.dataset.closeLabel || (isChinese ? '关闭导航' : 'Close navigation');
    const mobileViewport = window.matchMedia('(max-width: 820px)');

    const setMenuOpen = open => {
        menuToggle.setAttribute('aria-expanded', String(open));
        menuToggle.setAttribute('aria-label', open ? closeLabel : openLabel);
        menuToggle.setAttribute('title', open ? closeLabel : openLabel);
        primaryNav.classList.toggle('is-open', open);
    };

    const closeMenu = () => {
        setMenuOpen(false);
    };

    closeMenu();

    menuToggle.addEventListener('click', () => {
        setMenuOpen(menuToggle.getAttribute('aria-expanded') !== 'true');
    });

    primaryNav.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));

    document.addEventListener('keydown', event => {
        if (event.key === 'Escape' && menuToggle.getAttribute('aria-expanded') === 'true') {
            closeMenu();
            menuToggle.focus();
        }
    });

    document.addEventListener('click', event => {
        if (!menuToggle.contains(event.target) && !primaryNav.contains(event.target)) {
            closeMenu();
        }
    });

    mobileViewport.addEventListener('change', closeMenu);
}

const legacyPlayerCard = document.querySelector('#player-card');

if (legacyPlayerCard) {
    const cardFront = legacyPlayerCard.querySelector('.card-front');
    const cardBack = legacyPlayerCard.querySelector('.card-back');

    const flipLegacyCard = () => {
        const flipped = legacyPlayerCard.classList.toggle('flipped');
        legacyPlayerCard.setAttribute('aria-pressed', String(flipped));
        cardFront?.setAttribute('aria-hidden', String(flipped));
        cardBack?.setAttribute('aria-hidden', String(!flipped));
    };

    legacyPlayerCard.addEventListener('click', flipLegacyCard);
    legacyPlayerCard.addEventListener('keydown', event => {
        if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            flipLegacyCard();
        }
    });
}
