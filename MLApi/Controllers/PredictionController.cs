using Microsoft.AspNetCore.Mvc;
using System.Text;
using System.Text.Json;
using MLApi.Models;
using Microsoft.Extensions.Logging; // <-- Logger'ı kullanmak için

namespace MLApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class PredictionController : ControllerBase
    {
        private readonly HttpClient _httpClient;
        private readonly ILogger<PredictionController> _logger; // Logger eklendi

        public PredictionController(HttpClient httpClient, ILogger<PredictionController> logger)
        {
            _httpClient = httpClient;
            _logger = logger;
        }

        [HttpPost]
        public async Task<IActionResult> GetPrediction([FromBody] PredictionRequest requestData)
        {
            // Değişkenleri try bloğunun dışında tanımlayarak kapsama alanı sorununu çözüyoruz
            string pythonServiceUrl = "http://python-service:5000/predict"; 
            
            // 1. Python'ın beklediği JSON formatını oluştur
            var pythonPayload = new 
            {
                features = requestData.Features
            };
            
            var jsonString = JsonSerializer.Serialize(pythonPayload);
            var content = new StringContent(jsonString, Encoding.UTF8, "application/json");

            try
            {
                // 2. Python servisine POST isteği gönder
                var response = await _httpClient.PostAsync(pythonServiceUrl, content);

                // 3. Başarılı yanıtı döndür
                if (response.IsSuccessStatusCode)
                {
                    var responseBody = await response.Content.ReadAsStringAsync();
                    return Content(responseBody, "application/json");
                }
                else
                {
                    // 4. Python'dan gelen hata durumunu döndür
                    var errorBody = await response.Content.ReadAsStringAsync();
                    return StatusCode((int)response.StatusCode, $"Python Service Error: {errorBody}");
                }
            }
            catch (HttpRequestException ex)
            {
                // 5. Bağlantı hatasını yakala, logla ve 503 döndür
                _logger.LogError(ex, "Python servisine bağlanırken HATA oluştu.");
                return StatusCode(503, $"Hizmet kullanılamıyor (Python servisine erişilemiyor): {ex.Message}");
            }
        }
    }
}