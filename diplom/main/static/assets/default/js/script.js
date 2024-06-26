ymaps.ready(init);

function init() {
  var myMap = new ymaps.Map('map', {
    center: [55.753994, 37.622093],
    zoom: 9
  });
}

document.getElementById('myForm').addEventListener('submit', function(event) {
  // Отменяем отправку формы по умолчанию
  event.preventDefault();

  // Получаем значения полей формы
  var mehanik = document.getElementById('id_mehanik').value;
  var data = document.getElementById('id_data').value;
  var usluga = document.getElementById('id_usluga').value;
  var kater = document.getElementById('id_kater').value;

  // Проверяем, что все поля заполнены
  if (mehanik === '' || data === '' || usluga === '' || kater === '') {
    alert('Все поля обязательны для заполнения.');
    return;
  }

  // Проверяем, что дата ремонта не раньше текущей даты
  var currentDate = new Date();
  var selectedDate = new Date(data);
  if (selectedDate < currentDate) {
    alert('Дата ремонта не может быть раньше текущей даты.');
    return;
  }

  // Если все проверки пройдены, отправляем форму
  this.submit();
});
