using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http;
using Newtonsoft.Json;

namespace ApiCaller
{
    internal class Program
    {
        static void Main(string[] args)
        {
			using (HttpClient httpclient = new HttpClient())
			{
				try
				{
					Console.WriteLine("Buscador de productos");
					Console.WriteLine("Número 1: ");
					float numero1 = float.Parse(Console.ReadLine());
					Console.WriteLine("Numero 2: ");
					float numero2 = float.Parse(Console.ReadLine());
					String url = $"http://localhost/apis/suma.php?numero1={numero1}&numero2={numero2}";
					Console.WriteLine(url);
					HttpResponseMessage respuesta = httpclient.GetAsync(url).Result;
					string json = respuesta.Content.ReadAsStringAsync().Result;
					//Console.WriteLine(respuesta);
					var response = JsonConvert.DeserializeObject<MyApiResponse>(json);
					Console.WriteLine(response.result);
				}
				catch (Exception e)
				{

					Console.WriteLine($"Error al llamar API {e}");
				}
				finally
				{
					Console.ReadLine();
				}
			}
        }
    }

    class MyApiResponse
    {
        public float status { get; set; }
        public float result { get; set; }
    }
}
