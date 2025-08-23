// Bootstrap client-side validation
    (() => {
        'use strict'
        const forms = document.querySelectorAll('#addUserForm')
        Array.from(forms).forEach(form => {
            form.addEventListener('submit', event => {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }
                form.classList.add('was-validated')
            }, false)
        })
    })()

    $(document).ready(function() {
            // Edit button click
            $(".editBtn").click(function() {
                const userId = $(this).data("id");
              // Redirect without showing id in href
                window.location.href = "/edit/" + userId;
            });

            // Delete button click
            $(".deleteBtn").click(function() {
                const userId = $(this).data("id");
                if(confirm("Are you sure you want to delete this user?")) {
                // Redirect or send AJAX request
                window.location.href = "/delete/" + userId;
                }
            });
            });