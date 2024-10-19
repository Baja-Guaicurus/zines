window.addEventListener("DOMContentLoaded", () => {

	const websocket = new WebSocket("ws://localhost:12345/");

	websocket.onmessage = ({ data }) => {
		const json = JSON.parse(data)
		document.getElementById("rpm").innerHTML = "RPM: " + json["rpm"];
		document.getElementById("comb").innerHTML = "Combustível: " + json["comb"];
		document.getElementById("temp_cvt").innerHTML = "Temperatura da CVT: " + json["temp_cvt"];
		document.getElementById("velo").innerHTML = "Velocidade: " + json["velo"];
	};
});
