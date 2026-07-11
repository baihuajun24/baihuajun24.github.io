const menuToggle = document.querySelector('.menu-toggle');
const primaryNav = document.querySelector('#primary-nav');

if (menuToggle && primaryNav) {
    const closeMenu = () => {
        menuToggle.setAttribute('aria-expanded', 'false');
        menuToggle.setAttribute('aria-label', 'Open navigation');
        primaryNav.classList.remove('is-open');
    };

    menuToggle.addEventListener('click', () => {
        const open = menuToggle.getAttribute('aria-expanded') !== 'true';
        menuToggle.setAttribute('aria-expanded', String(open));
        menuToggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
        primaryNav.classList.toggle('is-open', open);
    });

    primaryNav.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
}

const profileCard = document.querySelector('#profile-card');

if (profileCard) {
    const front = profileCard.querySelector('.portrait-front');
    const back = profileCard.querySelector('.portrait-back');

    profileCard.addEventListener('click', () => {
        const flipped = profileCard.classList.toggle('is-flipped');
        profileCard.setAttribute('aria-pressed', String(flipped));
        front?.setAttribute('aria-hidden', String(flipped));
        back?.setAttribute('aria-hidden', String(!flipped));
    });
}

// Keep the legacy Chinese homepage interaction working during the transition.
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', event => {
        const target = document.querySelector(anchor.getAttribute('href'));
        if (!target) return;
        event.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
    });
});

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
