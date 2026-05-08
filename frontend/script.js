const BASE_URL = "http://127.0.0.1:8000";

let editApplicationId = null;

async function fetchApplications() {
    const response = await fetch(`${BASE_URL}/applications`);
    const applications = await response.json();

    displayApplications(applications);
}

function displayApplications(applications) {
    const container = document.getElementById("applicationsContainer");

    container.innerHTML = "";

    if (applications.length === 0) {
        container.innerHTML = `
            <p>No applications found.</p>
        `;
        return;
    }

    applications.forEach((application) => {
        const card = document.createElement("div");

        card.classList.add("application-card");

        card.innerHTML = `
            <h3>${application.company_name}</h3>
            <p><strong>Role:</strong> ${application.role}</p>
            <p>
                <strong>Status:</strong>
                <span class="status-badge ${application.status.toLowerCase()}">
                    ${application.status}
                </span>
            </p>
            <p><strong>Applied On:</strong> ${application.application_date}</p>
            <p><strong>Notes:</strong> ${application.notes || ""}</p>
            <p><strong>Follow-up:</strong> ${application.follow_up_date || ""}</p>

            <div class="action-buttons">
                <button onclick="editApplication(${application.id})">
                    Edit
                </button>

                <button onclick="deleteApplication(${application.id})">
                    Delete
                </button>
            </div>
        `;

        container.appendChild(card);
    });
}

async function fetchDashboardStats() {
    const response = await fetch(`${BASE_URL}/dashboard/stats`);
    const stats = await response.json();

    document.getElementById("total-count").textContent = stats.total;
    document.getElementById("applied-count").textContent = stats.applied;
    document.getElementById("interview-count").textContent = stats.interview;
    document.getElementById("rejected-count").textContent = stats.rejected;
    document.getElementById("selected-count").textContent = stats.selected;
}

document.getElementById("jobForm").addEventListener(
    "submit",
    async function (event) {
        event.preventDefault();

        const applicationData = {
            company_name: document.getElementById("company_name").value,
            role: document.getElementById("role").value,
            application_date: document.getElementById("application_date").value,
            status: document.getElementById("status").value,
            notes: document.getElementById("notes").value,
            follow_up_date: document.getElementById("follow_up_date").value
        };

        if (editApplicationId) {
            await fetch(
                `${BASE_URL}/applications/${editApplicationId}`,
                {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(applicationData)
                }
            );
            showMessage("Application updated successfully");
            document.querySelector("button[type='submit']").textContent =
            "Add Application";

            document.getElementById("searchInput").value = "";
            document.getElementById("filterStatus").value = "";

            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });



            editApplicationId = null;

        } else {
            await fetch(
                `${BASE_URL}/applications`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(applicationData)
                }
            );
            showMessage("Application added successfully");
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
            document.getElementById("searchInput").value = "";
            document.getElementById("filterStatus").value = "";
        }

        fetchApplications();
        fetchDashboardStats();

        document.getElementById("jobForm").reset();
    }
);

async function deleteApplication(id) {
    const confirmDelete = confirm(
        "Are you sure you want to delete this application?"
    );

    if (!confirmDelete) {
        return;
    }

    await fetch(`${BASE_URL}/applications/${id}`, {
        method: "DELETE"
    });

    showMessage("Application deleted successfully");

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
    
    fetchApplications();
    fetchDashboardStats();
}

fetchApplications();
fetchDashboardStats();

async function editApplication(id) {
    
    window.scrollTo({
                top: 200,
                behavior: "smooth"
            });

    document.querySelector("button[type='submit']").textContent =
    "Update Application";

    const response = await fetch(
        `${BASE_URL}/applications/${id}`
    );

    const application = await response.json();

    document.getElementById("company_name").value =
        application.company_name;

    document.getElementById("role").value =
        application.role;

    document.getElementById("application_date").value =
        application.application_date;

    document.getElementById("status").value =
        application.status;

    document.getElementById("notes").value =
        application.notes || "";

    document.getElementById("follow_up_date").value =
        application.follow_up_date || "";

    editApplicationId = id;

}   

document.getElementById("searchInput").addEventListener(
    "input",
    async function () {
        const keyword = this.value.trim();

        if (keyword === "") {
            fetchApplications();
            return;
        }

        const response = await fetch(
            `${BASE_URL}/applications/search?keyword=${keyword}`
        );

        const applications = await response.json();

        displayApplications(applications);
    }
);

document.getElementById("filterStatus").addEventListener(
    "change",
    async function () {
        const status = this.value;

        if (status === "") {
            fetchApplications();
            return;
        }

        const response = await fetch(
            `${BASE_URL}/applications?status=${status}`
        );

        const applications = await response.json();

        displayApplications(applications);
    }
);

function showMessage(message) {
    const messageBox = document.getElementById("messageBox");

    messageBox.textContent = message;
    messageBox.style.display = "block";

    setTimeout(() => {
        messageBox.style.display = "none";
    }, 3000);
}