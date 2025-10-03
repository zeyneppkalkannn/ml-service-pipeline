FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /src/MLApi  

COPY MLApi/MLApi.csproj . 
RUN dotnet restore

COPY MLApi/Controllers Controllers/
COPY MLApi/Program.cs .             
COPY MLApi/Models Models/

RUN dotnet build -c Release -o /app/build

FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS final
WORKDIR /app
COPY --from=build /app/build .

EXPOSE 8080 

ENTRYPOINT ["dotnet", "MLApi.dll"]