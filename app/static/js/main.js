document.getElementById('pyButton').addEventListener('click', async () => {
    const result = await eel.python_function()();
    document.getElementById('result').textContent = result;
});
