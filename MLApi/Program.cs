var builder = WebApplication.CreateBuilder(args);

// Docker içindeki .NET uygulamasını 8080 portunda dinlemeye zorlar.
// Bu, docker-compose.yml'deki "8080:8080" eşleşmesi için gereklidir.
builder.WebHost.UseUrls("http://*:8080"); 
// ************************************************************

// Add services to the container.
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// ÖNEMLİ: HttpClient servisini ekliyoruz
builder.Services.AddHttpClient();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseAuthorization();

app.MapControllers();

app.Run();