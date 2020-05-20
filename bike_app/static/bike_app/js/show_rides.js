
export function show_rides(response) {
    if (typeof(response) === 'string') {
                window.location.href = '/show_rides';
                var div = document.createElement("div");
                div.className = "container";
                document.body.appendChild(div);
            }
}