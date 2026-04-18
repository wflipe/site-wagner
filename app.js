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

    // Statistic count up - Globalizado para múltiplas seções (Fix da 3ª Seção e Impacto)
    const statsSections = document.querySelectorAll(".stats-trigger, #prova");
    statsSections.forEach(section => {
      ScrollTrigger.create({
        trigger: section,
        start: "top 80%",
        once: true,
        onEnter: () => {
          section.querySelectorAll(".counter").forEach((counter) => {
            // Suporta tanto data-target novo quanto data-val antigo
            const targetStr = counter.getAttribute("data-target") || counter.getAttribute("data-val");
            if (!targetStr) return;
            
            const targetVal = parseFloat(targetStr);
            const isDecimal = targetStr.includes(".") || counter.hasAttribute("data-dec");
            
            // Usamos um objeto proxy para o GSAP animar, evitando que o conteúdo HTML como "K+" ou "M" cause bugs no parsing numérico
            let proxy = { val: 0 };
            
            gsap.to(proxy, {
              val: targetVal,
              duration: 3.5,
              ease: "power3.out",
              onUpdate: function() {
                if (isDecimal) {
                  counter.innerHTML = proxy.val.toFixed(1);
                } else {
                  counter.innerHTML = Math.round(proxy.val).toLocaleString('pt-BR');
                }
              }
            });
          });
        }
      });
    });
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
