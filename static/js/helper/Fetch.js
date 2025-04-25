async function Fetch(id) {
    const data = await fetch(
        `http://127.0.0.1:8000/account/profile/bio/${id}/`,
        {
            body: JSON.stringify({
                bio: bioInput.value,
            }),
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
        }
    );
    const result = await data.json();
    const status = data.status;

    return {
        result,
        status,
    };
}
