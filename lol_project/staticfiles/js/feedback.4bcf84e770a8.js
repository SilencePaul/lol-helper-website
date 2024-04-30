document.addEventListener('DOMContentLoaded', function() {
    const formButton = document.getElementById('form-button');
    const feedbackForm = document.getElementById('feedback-form');
    formButton.addEventListener('click', function() {
        if (feedbackForm.classList.contains('is-hidden')) {
            feedbackForm.classList.remove('is-hidden');
            return;
        }
        feedbackForm.classList.add('is-hidden');
    });

    (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
        const $notification = $delete.parentNode;
    
        $delete.addEventListener('click', () => {
        $notification.parentNode.removeChild($notification);
        });
    });
});