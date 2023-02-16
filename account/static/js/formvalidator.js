/** Simple Form Validation */

/**
 * Input Validation
 *
 * @see https://daverupert.com/2017/11/happier-html5-forms/
 */
function inputValidator() {
    const inputs = document.querySelectorAll('input, select, textarea');
    for(let input of inputs) {
        input.addEventListener('invalid', (event) => {
            input.classList.add('error');
        }, false);

        input.addEventListener('blur', (event) => {
            input.checkValidity();
        });
    }
}

/**
 * Confirm Passwords
 *
 * @see https://codepen.io/diegoleme/pen/surIK
 */
function confirmPassword() {
    let password = document.getElementById("id_password1");
    let confirm = document.getElementById("id_password2");

    if (! password || ! confirm) {
        return false;
    }

    function validatePassword() {
        if (password.value != confirm.value) {
            confirm.setCustomValidity("Passwords do not match.");
        } else {
            confirm.setCustomValidity('');
        }
    }

    password.addEventListener('change', (event) => {
        validatePassword();
    });

    confirm.addEventListener('keyup', (event) => {
        validatePassword();
    });
}

document.addEventListener('DOMContentLoaded', function () {
    inputValidator();
    confirmPassword();
});
