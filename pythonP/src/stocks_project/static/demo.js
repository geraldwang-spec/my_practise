const random_url = "licensed-insights-indicated-competitive";
const API_URL = "https://" + random_url + ".trycloudflare.com";
async function connectToApi() {
  try {
    console.log("my test log")
    const response = await fetch(API_URL + "/test01", {
      method: "GET",
      headers: {
        "Content-Type": "application/json"
      }
    });

    const data = await response.json();
    console.log("from API get datas:", data);
    document.getElementById("apple").innerText = JSON.stringify(data);

  } catch (error) {
    console.error("connection fail", error);
  }

}

async function stocks_price() {
  try {
    const response = await fetch(API_URL + "/stocks_price");
    const data = await response.json();
    // const data = await fetch(API_URL + "/stocks_price").json()
    console.log(data.message);

    const stockArray = data.data || data;

    const listContainer = document.getElementById('stocks_list');
    if (!listContainer) {
      console.error("can't find stocks_list element");
      return;
    }

    // const htmlContent = data.map(data => `
    //   < tr >
    //     <td>${data.number}</td>
    //     <td>${data.id}</td>
    //     <td>${data.name}</td>
    //     <td>${data.price}</td>
    //   </tr >
    //   `).join();

    let html = '';
    stockArray.forEach(stock => {
      html += `
        <tr>
          <td>${stock.number}</td>
          <td>${stock.id}</td>
          <td>${stock.name}</td>
          <td>${stock.price}</td>
        </tr>
      `
    });
    listContainer.innerHTML = html;
    console.log("table OK");
  } catch (error) {
    console.error("get fail:", error);
  }
}
