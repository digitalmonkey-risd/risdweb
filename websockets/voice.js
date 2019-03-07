var msg = new SpeechSynthesisUtterance(document.getElementsByTagName("article"));
msg.voice = speechSynthesis.getVoices().filter(function(voice) { return voice.name == 'Whisper'; })[0];
speechSynthesis.speak(msg);