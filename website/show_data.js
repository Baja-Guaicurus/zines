window.addEventListener("DOMContentLoaded", () => {

	const websocket = new WebSocket("ws://localhost:12345/");

	websocket.onmessage = ({ data }) => {
		const json = JSON.parse(data)
		document.getElementById("velo").innerHTML = json["velo"];
		document.getElementById("temp").innerHTML = json["temp"];
	};
});
