window.addEventListener("DOMContentLoaded", () => {

	const websocket = new WebSocket("ws://localhost:12345/");

	websocket.onmessage = ({ data }) => {
		document.getElementById("random").innerHTML = data;
	};
});
