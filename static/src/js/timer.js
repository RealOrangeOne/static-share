function timer(display) {
  let duration = parseInt(display.data('duration'), 10);
  let minutes, seconds;
  const intervalId = setInterval(function () {
    minutes = parseInt(duration / 60, 10);
    seconds = parseInt(duration % 60, 10);

    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;

    const time = minutes + ':' + seconds;
    display.text(time);
    console.log(time);

    duration--;

    if (duration < 0) {
      clearInterval(intervalId);
      $('.download-button').addClass('btn-danger').removeClass('btn-primary').removeAttr('href');
      $('.timer-message').text('Link invalid - refresh the page to generate a new download link');
    }
  }, 1000);
}

$(document).ready(function () {
  timer($('.timer'));
});
