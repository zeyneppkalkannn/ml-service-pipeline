namespace MLApi.Models
{
    public class PredictionRequest
    {
        // Gelen JSON'daki "features" alanı ile eşleşir
        public List<List<double>> Features { get; set; } = new List<List<double>>();
    }
}
