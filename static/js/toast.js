const toastComponent = document.getElementById('toast-component');
const toastTitle = document.getElementById('toast-title');
const toastMessage = document.getElementById('toast-message');

function showToast(title, message, type = 'normal', duration = 3000) {
    
    if (!toastComponent) return;

    toastComponent.classList.remove(
        'bg-red-50', 'border-red-500', 'text-red-600',
        'bg-green-50', 'border-green-500', 'text-green-600',
        'bg-white', 'border-gray-300', 'text-gray-800',
        'bg-gray-200', 'border-blue-200', 'text-blue-200',
    );

    if (type === 'added') {
        toastComponent.classList.add('bg-gray-200', 'border-blue-200', 'text-blue-200');
        toastComponent.style.border = '1px solid #3e75e3';
    } else if (type === 'updated') {
        toastComponent.classList.add('bg-green-50', 'border-green-500', 'text-green-600');
        toastComponent.style.border;
    } else if (type === 'deleted') {
        toastComponent.classList.add('bg-red-50', 'border-red-500', 'text-red-600');
        toastComponent.style.border = '1px solid #ef4444';
    } else if (type === 'error') {
        toastComponent.classList.add('bg-red-50', 'border-red-500', 'text-red-600');
        toastComponent.style.border = '1px solid #ef4444';
    } else {
        toastComponent.classList.add('bg-white', 'border-gray-300', 'text-gray-800');
        toastComponent.style.border = '1px solid #d1d5db';
    }

    toastComponent.classList.remove('hidden');

    toastTitle.textContent = title;
    toastMessage.textContent = message;

    toastComponent.classList.remove('opacity-0', '-translate-y-4');
    toastComponent.classList.add('opacity-100', 'translate-y-0');

    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', '-translate-y-4');
        setTimeout(() => toastComponent.classList.add('hidden'), 300); // wait for animation
    }, duration);
}

function closeToast() {
  toastComponent.classList.remove('opacity-100', 'translate-y-0');
  toastComponent.classList.add('opacity-0', '-translate-y-4');
  setTimeout(() => toastComponent.classList.add('hidden'), 300); // wait for animation
}