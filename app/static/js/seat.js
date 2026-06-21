document.addEventListener("DOMContentLoaded", function () {
  let list_seats = [];
  let sum_total = 0;

  const station_seat = document.querySelector("#station strong");
  const price_seat = document.querySelector("#price strong");
  const button_payment = document.getElementById("go_to_payment");
  const seat_button = document.querySelectorAll(".seat button");

  const button_cancel = document.getElementById("btn_cancel");
  const button_back = document.getElementById("btn_back");

  function formatVND(amount) {
    return new Intl.NumberFormat("vi-VN", {
      style: "currency",
      currency: "VND",
    }).format(amount);
  }

  seat_button.forEach(function (button) {
    if (button.dataset.status === "NOT_AVAILABLE") {
      button.innerHTML = "";
      button.disabled = true;
      return;
    }

    button.addEventListener("click", function () {
      const seat_name = this.dataset.name;
      const seat_price = parseInt(this.dataset.price);

      const index = list_seats.indexOf(seat_name);

      if (index !== -1) {
        list_seats.splice(index, 1);
        sum_total -= seat_price;
        this.classList.remove("selected");
      } else {
        list_seats.push(seat_name);
        sum_total += seat_price;
        this.classList.add("selected");
      }

      if (list_seats.length > 0) {
        station_seat.innerHTML = list_seats.join(", ");
      } else {
        station_seat.innerHTML = "Chưa chọn";
      }

      price_seat.innerHTML = formatVND(sum_total);

      if (list_seats.length === 0) {
        button_payment.disabled = true;
        button_cancel.disabled = true;
      } else {
        button_payment.disabled = false;
        button_cancel.disabled = false;
      }
    });
  });

  button_cancel.addEventListener("click", function () {
    list_seats = [];
    sum_total = 0;

    seat_button.forEach(function (button) {
      button.classList.remove("selected");
    });

    station_seat.innerHTML = "Chưa chọn";
    price_seat.innerHTML = formatVND(sum_total);

    button_payment.disabled = true;
    button_cancel.disabled = true;
  });

  const payment_window = document.getElementById("open_payment_window");
  const close_outside = document.getElementById("close_outside");
  const close_with_x = document.getElementById("close_with_x");

  button_payment.addEventListener("click", function open_window() {
    const bank = "970415";
    const stk = "108883949880";

    const sum_total_seat = sum_total;
    let list_seat_payment = list_seats.join(" ");
    const content = `THANH TOAN GHE ${list_seat_payment}`;

    const img_second = "../static/bg/img/newqr.jpg";

    const urlQR =
      "https://img.vietqr.io/image/" +
      bank +
      "-" +
      stk +
      "-compact.png?amount=" +
      sum_total_seat +
      "&addInfo=" +
      encodeURIComponent(content);

    const qrImage = document.getElementById("qr-bank");

    qrImage.onerror = function () {
      this.onerror = null;
      this.src = img_second;
    };

    qrImage.src = urlQR;

    payment_window.style.display = "block";
    close_outside.style.display = "block";
  });

  close_with_x.addEventListener("click", function close_window() {
    payment_window.style.display = "none";
    close_outside.style.display = "none";
  });

  close_outside.addEventListener("click", function close_window() {
    payment_window.style.display = "none";
    close_outside.style.display = "none";
  });
  const buy = document.getElementById("buy");

  const username = bill.dataset.username;
  const email = bill.dataset.email;
  buy.addEventListener("click", function inf_buy() {
    bill = document.getElementById("bill");
    bill.style.display = "block";
    payment_window.style.display = "none";
    close_outside.style.display = "none";

    bill.innerHTML = `<div class="invoice" style="border: 1px dashed #333; padding: 15px; background-color: #f9f9f9;">
        <h3 style="color:black">HÓA ĐƠN THANH TOÁN</h3>
        <p style="color:black"><strong>Khách hàng:</strong> ${username}</p>
        <p style="color:black"><strong>Email:</strong> ${email}</p>
        <hr>
        <p style="color:black"><strong>Danh sách ghế:</strong> ${list_seats.join(", ")}</p>
        <p style="color:black"><strong>Tổng tiền:</strong> <span style="color: red; font-weight: bold;">${formatVND(sum_total)}</span></p>
        <p style="font-style: italic; font-size: 12px; color: green;">Trạng thái: Thanh toán thành công</p>
      </div>
    `;
    const list_seats_user_buy = document.getElementById("list_seat_user_buy");
    list_seats_user_buy.value = list_seats;
  });
});
