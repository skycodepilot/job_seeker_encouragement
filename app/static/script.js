document.getElementById("fetch").addEventListener("click", async () => {
    const city = document.getElementById("city").value;
    const endpoint = city ? 
      `/encouragement/${city}` : 
      `/encouragement`;
  
    const res = await fetch(endpoint);
    const data = await res.json();
    document.getElementById("result").innerText = data.encouragement;
  });
  