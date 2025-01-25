function filterSchemes() {
    const age = document.getElementById('age').value;
    const purpose = document.getElementById('purpose').value;
    const schemes = document.querySelectorAll('.scheme');

    schemes.forEach(scheme => {
        const schemeAge = scheme.getAttribute('data-age');
        const schemePurpose = scheme.getAttribute('data-purpose');

        if ((age === "" || schemeAge === age) && (purpose === "" || schemePurpose === purpose)) {
            scheme.style.display = "block";
        } else {
            scheme.style.display = "none";
        }
    });
}

function showDetails(element, title, description) {
    const detailsContainer = document.getElementById('scheme-details');
    const titleElement = document.getElementById('scheme-title');
    const descriptionElement = document.getElementById('scheme-description');

    titleElement.textContent = title;
    descriptionElement.textContent = description;

    const isLeftColumn = element.parentElement.classList.contains('left-column');
    const descriptionParent = detailsContainer.parentElement;

    if (isLeftColumn) {
        descriptionParent.style.justifyContent = 'flex-start';
    } else {
        descriptionParent.style.justifyContent = 'flex-end';
    }
}
