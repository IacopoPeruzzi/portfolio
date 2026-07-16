import { useEffect, useLayoutEffect, useState } from 'react';

const introMessages = [
  'Hi. I’m Iacopo',
  'a UX & Service Design Manager',
  'I lead design across products, services and systems',
  'to turn complex technology into experiences people trust and businesses scale.',
  'That’s what I design for.',
];

const Hero = () => {
  const [introState, setIntroState] = useState('playing');
  const [activeMessage, setActiveMessage] = useState(0);
  const [typedCharacters, setTypedCharacters] = useState(0);

  useLayoutEffect(() => {
    document.body.classList.toggle('is-hero-introducing', introState !== 'complete');
    return () => document.body.classList.remove('is-hero-introducing');
  }, [introState]);

  useEffect(() => {
    if (introState === 'complete') return undefined;

    if (introState === 'exiting') {
      const completeTimer = window.setTimeout(() => setIntroState('complete'), 1450);
      return () => window.clearTimeout(completeTimer);
    }

    const activeText = introMessages[activeMessage];
    if (typedCharacters < activeText.length) {
      const typingTimer = window.setTimeout(() => {
        setTypedCharacters((characters) => characters + 1);
      }, 55);
      return () => window.clearTimeout(typingTimer);
    }

    if (activeMessage < introMessages.length - 1) {
      const nextMessageTimer = window.setTimeout(() => {
        setActiveMessage((message) => message + 1);
        setTypedCharacters(0);
      }, 1150);
      return () => window.clearTimeout(nextMessageTimer);
    }

    const exitTimer = window.setTimeout(() => setIntroState('exiting'), 1350);
    return () => window.clearTimeout(exitTimer);
  }, [activeMessage, introState, typedCharacters]);

  const isIntroducing = introState !== 'complete';

  return (
    <section className={`section hero ${isIntroducing ? 'is-introducing' : 'is-ready'} ${introState === 'exiting' ? 'is-intro-exiting' : ''}`}>
      {isIntroducing && (
        <div className={`hero-intro ${introState === 'exiting' ? 'is-exiting' : ''}`} aria-hidden="true">
          <div className={`container hero-intro__stage ${activeMessage > 0 ? 'has-history' : ''}`}>
            {introMessages.slice(Math.max(0, activeMessage - 1), activeMessage + 1).map((message, index, messages) => {
              const position = messages.length - index - 1;
              const isCurrent = position === 0;
              return (
                <p
                  className={`hero-intro__message ${isCurrent ? 'is-current' : 'is-history'}`}
                  key={message}
                >
                  {isCurrent ? message.slice(0, typedCharacters) : message}
                </p>
              );
            })}
          </div>
        </div>
      )}

      <div className="container hero-content">
        <h1 className="hero-final-title"><span>Designing experiences</span><span>that matter.</span></h1>
        <div className="hero-actions">
          <a className="button button-primary" href="#initiatives">Explore selected work <span aria-hidden="true">↘</span></a>
          <a className="button button-quiet" href="#contact">Start a conversation <span aria-hidden="true">→</span></a>
        </div>
      </div>
    </section>
  );
};

export default Hero;
