// ===== FORCE RESET localStorage (xóa dữ liệu cũ) =====
// Chạy ngay khi script load để đảm bảo dùng dữ liệu mới nhất
(function () {
  localStorage.removeItem("products");
  localStorage.removeItem("products_version");
})();

// Danh sách sản phẩm mặc định (sử dụng khi localStorage chưa có dữ liệu)
// Phiên bản dữ liệu sản phẩm - tăng lên khi có thay đổi về cấu trúc dữ liệu
const PRODUCTS_DATA_VERSION = 3;

const products = [
  {
    id: 1,
    name: "Fire & Ash Cup",
    price: 199000,
    image: "../static/img/1.jpg",
    category: "movie-verse",
    starGroup: "Cốc / Ly",
  },
  {
    id: 2,
    name: "Fish & Ash Set",
    price: 249000,
    image: "../static/img/2.jpg",
    category: "movie-verse",
    starGroup: "Combo / Set",
  },
  {
    id: 3,
    name: "Zootopia Cup",
    price: 199000,
    image: "../static/img/3.jpg",
    category: "movie-verse",
    starGroup: "Cốc / Ly",
  },
  {
    id: 4,
    name: "Doraemon Face Pouch Keychain...",
    price: 199000,
    image: "../static/img/4.png",
    category: "wibu",
    starGroup: "Phụ kiện",
  },
  {
    id: 5,
    name: "Doraemon Face Pouch Keychain",
    price: 199000,
    image: "../static/img/5.png",
    category: "wibu",
    starGroup: "Móc khóa",
  },
  {
    id: 6,
    name: "Jujutsu Kaisen Bobblehead",
    price: 199000,
    image: "../static/img/6.jpg",
    category: "wibu",
    starGroup: "Đồ chơi / Figure",
  },
  {
    id: 7,
    name: "Jujutsu Kaisen Bobblehead Set",
    price: 249000,
    image: "../static/img/7.jpg",
    category: "wibu",
    starGroup: "Combo / Set",
  },
  {
    id: 8,
    name: "Ly nước Capybara",
    price: 350000,
    image: "../static/img/8.jpg",
    category: "inner-child",
    starGroup: "Cốc / Ly",
  },
  {
    id: 9,
    name: "BTS ARIRANG Popcorn Tin",
    price: 275000,
    image: "../static/img/9.jpg",
    category: "yolo",
    starGroup: "Bắp rang / Khác",
  },
  {
    id: 10,
    name: "Fanta",
    price: 275000,
    image: "../static/img/10.jpg",
    category: "yolo",
    starGroup: "Nước Ngọt",
  },
  {
    id: 11,
    name: "Coca",
    price: 275000,
    image: "../static/img/11.png",
    category: "yolo",
    starGroup: "Nước Ngọt",
  },
  {
    id: 12,
    name: "Sprite",
    price: 275000,
    image: "../static/img/12.png",
    category: "yolo",
    starGroup: "Nước Ngọt",
  },
  {
    id: 13,
    name: "Coca Zero",
    price: 275000,
    image: "../static/img/13.png",
    category: "yolo",
    starGroup: "Nước Ngọt",
  },
  {
    id: 14,
    name: "Dasani",
    price: 275000,
    image: "../static/img/14.png",
    category: "yolo",
    starGroup: "Nước Ngọt",
  },
  {
    id: 15,
    name: "Nutri Boost",
    price: 275000,
    image: "../static/img/15.png",
    category: "yolo",
    starGroup: "Nước Ngọt",
  },
  {
    id: 16,
    name: "Nước Cam Ép Teppy",
    price: 275000,
    image: "../static/img/16.png",
    category: "yolo",
    starGroup: "Nước Ngọt",
  },
  {
    id: 17,
    name: "Lay's Khoai Tây",
    price: 275000,
    image: "../static/img/17.png",
    category: "yolo",
    starGroup: "Bim Bim",
  },
  {
    id: 18,
    name: "Lay's Khoai Tây Vàng",
    price: 275000,
    image: "../static/img/18.png",
    category: "yolo",
    starGroup: "Bim Bim",
  },
  {
    id: 19,
    name: "Lay's Khoai Tây Đỏ",
    price: 275000,
    image: "../static/img/19.png",
    category: "yolo",
    starGroup: "Bim Bim",
  },
];

// Khởi tạo dữ liệu sản phẩm vào localStorage
// Nếu chưa có dữ liệu hoặc phiên bản cũ thì xóa cũ và ghi đè dữ liệu mới
function initProducts() {
  const savedVersion = localStorage.getItem("products_version");
  if (
    !localStorage.getItem("products") ||
    savedVersion != PRODUCTS_DATA_VERSION
  ) {
    localStorage.removeItem("products");
    localStorage.setItem("products", JSON.stringify(products));
    localStorage.setItem("products_version", PRODUCTS_DATA_VERSION);
    console.log(
      "Đã cập nhật dữ liệu sản phẩm lên phiên bản " + PRODUCTS_DATA_VERSION,
    );
  }
}

// Lấy danh sách sản phẩm từ localStorage (nếu không có trả về mảng `products` mặc định)
function getProducts() {
  return JSON.parse(localStorage.getItem("products")) || products;
}
// Khởi tạo giỏ hàng trong localStorage nếu chưa tồn tại
function initCart() {
  if (!localStorage.getItem("cart")) {
    localStorage.setItem("cart", JSON.stringify([]));
  }
}

// Lấy giỏ hàng từ localStorage
function getCart() {
  return JSON.parse(localStorage.getItem("cart")) || [];
}

// Thêm sản phẩm vào giỏ hàng (nếu đã có thì tăng số lượng)
function addToCart(productId, quantity = 1) {
  const cart = getCart();
  const product = getProducts().find((p) => p.id === productId);
  if (!product) return;

  const existingItem = cart.find((item) => item.id === productId);
  if (existingItem) {
    existingItem.quantity += quantity;
  } else {
    cart.push({
      id: product.id,
      name: product.name,
      price: product.price,
      quantity: quantity,
    });
  }
  localStorage.setItem("cart", JSON.stringify(cart));
  console.log(`Đã thêm "${product.name}" vào giỏ hàng. Số lượng: ${quantity}`);
  renderCart("cart-container");
  updateCartCountUI();
}

// Xóa sản phẩm khỏi giỏ hàng
function removeFromCart(productId) {
  let cart = getCart();
  cart = cart.filter((item) => item.id !== productId);
  localStorage.setItem("cart", JSON.stringify(cart));
  console.log(`Đã xóa sản phẩm khỏi giỏ hàng`);
  renderCart("cart-container");
  updateCartCountUI();
}

// Cập nhật số lượng sản phẩm trong giỏ hàng
function updateCartQuantity(productId, quantity) {
  const cart = getCart();
  const item = cart.find((item) => item.id === productId);
  if (item) {
    item.quantity = quantity;
    if (quantity <= 0) {
      removeFromCart(productId);
    } else {
      localStorage.setItem("cart", JSON.stringify(cart));
      renderCart("cart-container");
      updateCartCountUI();
    }
  }
}

// Render cart contents into container with id `containerId` (if present)
function renderCart(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  const cart = getCart();
  if (!cart || cart.length === 0) {
    container.innerHTML = '<p class="cart-empty">Giỏ hàng đang trống</p>';
    updateCartTotalUI(0);
    updateCartCountUI();
    return;
  }

  container.innerHTML = cart
    .map((item) => {
      const subtotal = item.price * item.quantity;
      return `
      <div class="cart-item" data-id="${item.id}">
        <div class="cart-item-name">${item.name}</div>
        <div class="cart-item-controls">
          <button class="decrease-qty" data-product-id="${item.id}">-</button>
          <span class="cart-item-qty">${item.quantity}</span>
          <button class="increase-qty" data-product-id="${item.id}">+</button>
        </div>
        <div class="cart-item-subtotal">${subtotal.toLocaleString()} đ</div>
        <button class="remove-from-cart-btn" data-product-id="${item.id}">Xóa</button>
      </div>
    `;
    })
    .join("");

  updateCartTotalUI(calculateCartTotal());
  updateCartCountUI();
}

function updateCartCountUI() {
  const el = document.getElementById("cart-count");
  if (el) el.textContent = getCartItemCount();
}

function updateCartTotalUI(total) {
  const el = document.getElementById("cart-total");
  if (el) el.textContent = (total || 0).toLocaleString() + " đ";
}

// Tính tổng tiền giỏ hàng
function calculateCartTotal() {
  const cart = getCart();
  return cart.reduce((total, item) => total + item.price * item.quantity, 0);
}

// Tính tổng số lượng sản phẩm trong giỏ hàng
function getCartItemCount() {
  const cart = getCart();
  return cart.reduce((count, item) => count + item.quantity, 0);
}

// Hiển thị (render) các sản phẩm theo `category` vào DOM container có id `containerId`
function renderProductsByCategory(containerId, category) {
  const container = document.getElementById(containerId);
  if (!container) return;
  const list = getProducts().filter((p) => p.category === category);
  container.innerHTML = list
    .map(
      (p) => `
    <div class="product-card" id="${p.id}" category="${p.category}">
      <img src="${p.image}" alt="${p.name}" />
      <p class="name">${p.name}</p>
      <p class="price">${p.price.toLocaleString()} đ</p>
      <button class="add-to-cart-btn" data-product-id="${p.id}">Thêm vào giỏ</button>
    </div>
  `,
    )
    .join("");
}

// Hiển thị (render) Star Shop - chia theo nhóm, mỗi sản phẩm 1 hàng ngang
function renderStarShop(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  const list = getProducts();

  // Lấy danh sách các nhóm duy nhất
  const groups = [...new Set(list.map((p) => p.starGroup))];

  let html = "";
  groups.forEach((group) => {
    const items = list.filter((p) => p.starGroup === group);
    // Tạo các card ngang xếp trong flex-wrap
    html += `
      <div class="star-group">
        <h3 class="star-group-title">${group}</h3>
        <div class="star-group-horizontal">
          ${items
            .map(
              (p) => `
            <div class="product-card-horizontal" id="${p.id}" category="${p.category}">
              <div class="product-horizontal-img">
                <img src="${p.image}" alt="${p.name}" />
              </div>
              <div class="product-horizontal-info">
                <p class="name">${p.name}</p>
                <p class="price">${p.price.toLocaleString()} đ</p>
                <button class="add-to-cart-btn" data-product-id="${p.id}">Thêm vào giỏ</button>
              </div>
            </div>
          `,
            )
            .join("")}
        </div>
      </div>
    `;
  });

  container.innerHTML = html;
}

// Hiển thị (render) tất cả sản phẩm (dạng phẳng, không nhóm - dùng cho search)
function renderAllProducts(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  const list = getProducts();
  container.innerHTML = list
    .map(
      (p) => `
    <div class="product-card" id="${p.id}" category="${p.category}">
      <img src="${p.image}" alt="${p.name}" />
      <p class="name">${p.name}</p>
      <p class="price">${p.price.toLocaleString()} đ</p>
      <button class="add-to-cart-btn" data-product-id="${p.id}">Thêm vào giỏ</button>
    </div>
  `,
    )
    .join("");
}

// Tìm kiếm sản phẩm theo từ khóa (tìm trong tên và danh mục sản phẩm)
function searchProducts(query) {
  if (!query.trim()) {
    renderStarShop("star-products");
    return;
  }
  const list = getProducts();
  const filtered = list.filter(
    (p) =>
      p.name.toLowerCase().includes(query.toLowerCase()) ||
      p.category.toLowerCase().includes(query.toLowerCase()),
  );
  const container = document.getElementById("star-products");
  if (!container) return;
  container.innerHTML = filtered
    .map(
      (p) => `
    <div class="product-card" id="${p.id}" category="${p.category}">
      <img src="${p.image}" alt="${p.name}" />
      <p class="name">${p.name}</p>
      <p class="price">${p.price.toLocaleString()} đ</p>
      <button class="add-to-cart-btn" data-product-id="${p.id}">Thêm vào giỏ</button>
    </div>
  `,
    )
    .join("");
}

// Khi DOM đã sẵn sàng: khởi tạo dữ liệu, render các vùng sản phẩm, và thiết lập sự kiện tìm kiếm
document.addEventListener("DOMContentLoaded", function () {
  initProducts();
  initCart();
  // console.log("products.js loaded, products count=", getProducts().length);
  renderStarShop("star-products");
  renderProductsByCategory("movies-products", "movie-verse");
  renderProductsByCategory("wibu-products", "wibu");
  renderProductsByCategory("inner-child-products", "inner-child");
  renderProductsByCategory("yolo-products", "yolo");
  // Hiển thị và update count/total
  renderCart("cart-container");
  updateCartCountUI();

  // Lắng nghe sự kiện click nút search
  const searchBtn = document.getElementById("search-btn");
  const searchInput = document.getElementById("searchInput");
  if (searchBtn) {
    searchBtn.addEventListener("click", function () {
      searchProducts(searchInput.value);
    });
  }

  // Lắng nghe sự kiện nhấn Enter trong ô tìm kiếm
  if (searchInput) {
    searchInput.addEventListener("keypress", function (e) {
      if (e.key === "Enter") {
        searchProducts(searchInput.value);
      }
    });
  }

  // Event delegation: lắng nghe click cho nút thêm/xóa/ tăng giảm số lượng
  document.addEventListener("click", function (e) {
    if (e.target.classList.contains("add-to-cart-btn")) {
      const productId = parseInt(e.target.getAttribute("data-product-id"));
      addToCart(productId, 1);
      alert("Đã thêm sản phẩm vào giỏ hàng!");
      return;
    }

    if (e.target.classList.contains("remove-from-cart-btn")) {
      const productId = parseInt(e.target.getAttribute("data-product-id"));
      removeFromCart(productId);
      return;
    }

    if (e.target.classList.contains("increase-qty")) {
      const productId = parseInt(e.target.getAttribute("data-product-id"));
      const cart = getCart();
      const item = cart.find((it) => it.id === productId);
      if (item) updateCartQuantity(productId, item.quantity + 1);
      return;
    }

    if (e.target.classList.contains("decrease-qty")) {
      const productId = parseInt(e.target.getAttribute("data-product-id"));
      const cart = getCart();
      const item = cart.find((it) => it.id === productId);
      if (item) updateCartQuantity(productId, item.quantity - 1);
      return;
    }
  });
});

// Chuyển đổi hiển thị giữa các trang danh mục:
//  - Ẩn tất cả `.page`
//  - Hiện trang được chọn theo `idCanHien`
//  - Cập nhật class `active` cho nút được bấm
function showShopContent(idCanHien, btnElement) {
  const cactrang = document.querySelectorAll(".page");
  cactrang.forEach((trang) => {
    trang.style.display = "none";
  });

  const buttons = document.querySelectorAll(".shop-btn");
  buttons.forEach((btn) => {
    btn.classList.remove("active");
  });

  document.getElementById(idCanHien).style.display = "block";

  btnElement.classList.add("active");
}
