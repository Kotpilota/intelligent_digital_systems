 // Обработка уведомлений
 document.getElementById('notifications').addEventListener('click', () => {
    alert('Новых уведомлений нет');
  });

  // Анимация появления карточек статистики
  document.addEventListener('DOMContentLoaded', () => {
    const statsCards = document.querySelectorAll('.stats-card');
    statsCards.forEach((card, index) => {
      card.style.animationDelay = `${index * 0.1}s`;
    });
  });

  // Интерактивность проектных карточек
  const projectCards = document.querySelectorAll('.project-card');
  projectCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      card.style.transform = 'translateY(-4px)';
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'translateY(0)';
    });
  });