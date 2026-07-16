
import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

const useThemeSwitcher = () => {
  const { pathname } = useLocation();

  useEffect(() => {
    // Force light mode for case studies
    if (pathname.startsWith('/case-study/')) {
      document.body.classList.add('is-light');
      return () => document.body.classList.remove('is-light');
    }

    const checkTheme = () => {
      const lightSections = document.querySelectorAll('.section-light');
      const scrollY = window.scrollY;
      const windowMid = scrollY + (window.innerHeight * 0.5);
      
      let bodyShouldBeLight = false;
      let headerShouldBeLight = false;

      lightSections.forEach(section => {
        const top = section.offsetTop;
        const height = section.offsetHeight;
        
        // Body theme (based on center of screen)
        if (windowMid >= top && windowMid <= top + height) {
          bodyShouldBeLight = true;
        }

        // Header theme (based on top of screen)
        if (scrollY + 40 >= top && scrollY + 40 <= top + height) {
          headerShouldBeLight = true;
        }
      });

      if (bodyShouldBeLight) {
        document.body.classList.add('is-light');
      } else {
        document.body.classList.remove('is-light');
      }

      if (headerShouldBeLight) {
        document.body.classList.add('header-light');
      } else {
        document.body.classList.remove('header-light');
      }
    };

    let animationFrame;
    const handleScroll = () => {
      if (animationFrame) return;
      animationFrame = window.requestAnimationFrame(() => {
        checkTheme();
        animationFrame = undefined;
      });
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    checkTheme();

    return () => {
      window.removeEventListener('scroll', handleScroll);
      if (animationFrame) window.cancelAnimationFrame(animationFrame);
      document.body.classList.remove('is-light');
      document.body.classList.remove('header-light');
    };
  }, [pathname]);
};

export default useThemeSwitcher;
