let allJobs = []

function renderJobs(jobs) {
    const container = document.querySelector(".job-list");
    container.innerHTML = '';

    if (jobs.length === 0) {
        container.innerHTML = '<p class="no-jobs">Нет подходящих вакансий</p>';
        return;
    }

    jobs.forEach(job => {
        const card = createJobCard(job);
        container.appendChild(card);
    });
}

function applyFilters() {
    const form = document.querySelector('.filters__form');
    const position = form.elements.position.value.trim().toLowerCase();
    const city = form.elements.city.value.trim().toLowerCase();
    const employmentType = form.elements.employmentType.value.toLowerCase();
    const level = form.elements.level.value.toLowerCase();

    const filteredJobs = allJobs.filter(job => {
        const jobPosition = job.position?.toLowerCase() || '';
        const jobCity = job.location?.city?.toLowerCase() || '';
        const jobEmployment = job.employment_type?.type.toLowerCase() || '';
        const jobLevel = job.employment_level?.level?.toLowerCase() || '';

        const matchesPosition = jobPosition.includes(position);
        const matchesCity = jobCity.includes(city);
        const matchesEmployment = !employmentType || jobEmployment === employmentType;
        const matchesLevel = !level || jobLevel === level;

        return matchesPosition && matchesCity && matchesEmployment && matchesLevel;
    });

    renderJobs(filteredJobs);
}
function createJobCard(job) {
    const article = document.createElement("article");
    article.className = "job-card";

    const title = document.createElement("h2");
    title.className = "job-card__title";
    title.textContent = job.position || 'Без названия';

    const company = document.createElement("div");
    company.className = "job-card__company";
    company.textContent = job.company || 'Компания не указана';
    
    const details = document.createElement("div");
    details.className = "job-card__details";

    const createDetail = (iconPath, text) => {
        const span = document.createElement("span");
        span.className = "job-card__detail";
        
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        svg.setAttribute("width", "16");
        svg.setAttribute("height", "16");
        svg.setAttribute("viewBox", "0 0 24 24");
        svg.setAttribute("fill", "none");
        svg.setAttribute("stroke", "currentColor");
        svg.innerHTML = iconPath;
        
        span.append(svg, ` ${text || 'Не указано'}`);
        return span;
    };

    details.append(
        createDetail(
            '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/>',
            job.location?.city || 'Город не указан'
        ),
        createDetail(
            '<rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v16"/>',
            job.employment_type?.type || 'Тип занятости не указан'  
        ),
        createDetail(
            '<path d="M12 2v20M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/>',
            job.salary ? `от ${job.salary} ₽` : 'З/П не указана'
        )
    );

    const description = document.createElement("p");
    description.className = "job-card__description";
    description.textContent = job.description || 'Описание отсутствует';

    const button = document.createElement("a");
    button.className = "button";
    button.textContent = "Откликнуться";
    button.href = `/job_application_page/${job.id}`;
    

    button.addEventListener('click', () => {
        window.location.href(`/job_application`);
    });
    
    article.append(title, company, details, description, button);
    return article;
}

async function getJobs() {
    try {
        const response = await fetch('/job/read', {
            method: 'GET',
            headers: {
                'Accept': 'application/json'
            },
        });

        if (!response.ok) throw new Error(`Ошибка HTTP: ${response.status}`);

        allJobs = await response.json();
        renderJobs(allJobs);
    } catch (error) {
        console.error("Ошибка при загрузке вакансий:", error);
        const container = document.querySelector(".job-list");
        if (container) {
            container.innerHTML = `<p class="error-message">Ошибка загрузки данных: ${error.message}</p>`;
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelector(".search-button").addEventListener("click", function(event) {
        event.stopPropagation();
        const search = document.querySelector(".search");
        search.style.width = "200px";
        search.style.marginLeft = "20px";
    });

    document.querySelector(".search").addEventListener("click", function(event) {
        event.stopPropagation();
    });

    
    document.querySelector('.filters__form').addEventListener('input', applyFilters);

    window.addEventListener("click", function() {
        const search = document.querySelector(".search");
        search.style.width = "0px";
        search.style.marginLeft = "0px";
    });

    getJobs();
});
