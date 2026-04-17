/**
 * Wagner Filipe - IA Especializada
 * Scripts Principais
 */

document.addEventListener("DOMContentLoaded", () => {
  // GSAP Animations (Animações Leves e Otimizadas)
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);

    // Fade up staggered animation
    const revealElements = document.querySelectorAll(".gsap-reveal");
    revealElements.forEach((el) => {
      gsap.fromTo(el, 
        { y: 40, opacity: 0 },
        { 
          y: 0, 
          opacity: 1, 
          duration: 1, 
          ease: "power3.out",
          scrollTrigger: {
            trigger: el,
            start: "top 85%",
            toggleActions: "play none none none"
          }
        }
      );
    });

    // Statistic count up
    const statsTrigger = document.querySelector(".stats-trigger");
    if (statsTrigger) {
      ScrollTrigger.create({
        trigger: statsTrigger,
        start: "top 80%",
        once: true,
        onEnter: () => {
          document.querySelectorAll(".counter").forEach((counter) => {
            const target = parseFloat(counter.getAttribute("data-val"));
            const isDecimal = counter.hasAttribute("data-dec");
            
            gsap.to(counter, {
              innerHTML: target,
              duration: 2.5,
              ease: "power2.out",
              snap: { innerHTML: isDecimal ? 0.1 : 1 },
              onUpdate: function() {
                counter.innerHTML = isDecimal 
                  ? Number(this.targets()[0].innerHTML).toFixed(1)
                  : Math.round(this.targets()[0].innerHTML);
              }
            });
          });
        }
      });
    }
  }

  // Smooth Scrolling for Anchor Links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        window.scrollTo({
          top: target.offsetTop - 80, // Offset for sticky navbar
          behavior: 'smooth'
        });
      }
    });
  });

  // Form Handling - Arquitetura Aberta para Automação (Webhooks)
  const formEntry = document.getElementById("leadForm");
  if (formEntry) {
    formEntry.addEventListener("submit", (e) => {
      // By default, Netlify handles it because of data-netlify="true" in HTML
      // But we can add custom webhook dispatches here without gambiarras
      
      const submitBtn = formEntry.querySelector('button[type="submit"]');
      const originalText = submitBtn.innerHTML;
      
      // UX Feedback
      submitBtn.innerHTML = `Criando Agendamento...`;
      submitBtn.style.opacity = 0.8;
      submitBtn.style.pointerEvents = "none";
      
      // Let standard form submission continue
      setTimeout(() => {
        submitBtn.innerHTML = originalText;
        submitBtn.style.opacity = 1;
        submitBtn.style.pointerEvents = "auto";
      }, 2000);
    });
  }
});
