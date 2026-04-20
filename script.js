async function loadMembers() {
  const response = await fetch("./members.json", { cache: "no-store" });
  if (!response.ok) {
    throw new Error(`成员数据读取失败: ${response.status}`);
  }
  return response.json();
}

function renderMembers(members) {
  const grid = document.getElementById("cardGrid");
  const tpl = document.getElementById("cardTemplate");

  members.forEach((member, i) => {
    const node = tpl.content.cloneNode(true);
    node.querySelector(".member-index").textContent = `#${String(i + 1).padStart(2, "0")}`;
    node.querySelector(".member-name").textContent = member.name;
    node.querySelector(".member-role").textContent = member.role || "402 成员";
    node.querySelector(".member-note").textContent = member.note || "欢迎回家";
    const card = node.querySelector(".member-card");
    card.style.animationDelay = `${i * 80}ms`;
    grid.appendChild(node);
  });
}

async function bootstrap() {
  try {
    const members = await loadMembers();
    renderMembers(members);
  } catch (err) {
    const grid = document.getElementById("cardGrid");
    grid.innerHTML = `<article class="member-card"><h2>加载失败</h2><p>${String(err.message || err)}</p></article>`;
  }
}

bootstrap();
