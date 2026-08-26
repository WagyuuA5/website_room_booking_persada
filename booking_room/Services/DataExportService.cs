using System.Text;
using System.Reflection;
using ClosedXML.Excel;

namespace booking_room.Services
{
    public class DataExportService
    {
        public byte[] ExportToCsv<T>(IEnumerable<T> data)
        {
            var properties = typeof(T).GetProperties(BindingFlags.Public | BindingFlags.Instance)
                .Where(p => p.CanRead)
                .ToList();

            var sb = new StringBuilder();

            // Header
            var headers = properties.Select(p => EscapeCsv(p.Name));
            sb.AppendLine(string.Join(",", headers));

            // Data
            foreach (var item in data)
            {
                var values = properties.Select(p => 
                {
                    var val = p.GetValue(item);
                    return EscapeCsv(val?.ToString() ?? "");
                });
                sb.AppendLine(string.Join(",", values));
            }

            return Encoding.UTF8.GetBytes(sb.ToString());
        }

        public byte[] ExportToExcel<T>(IEnumerable<T> data, string sheetName = "Data")
        {
            using var workbook = new XLWorkbook();
            var worksheet = workbook.Worksheets.Add(sheetName);
            
            var properties = typeof(T).GetProperties(BindingFlags.Public | BindingFlags.Instance)
                .Where(p => p.CanRead)
                .ToList();

            // Header
            for (int i = 0; i < properties.Count; i++)
            {
                var cell = worksheet.Cell(1, i + 1);
                cell.Value = properties[i].Name;
                cell.Style.Font.Bold = true;
                cell.Style.Fill.BackgroundColor = XLColor.LightGray;
            }

            // Data
            int row = 2;
            foreach (var item in data)
            {
                for (int i = 0; i < properties.Count; i++)
                {
                    var val = properties[i].GetValue(item);
                    var cell = worksheet.Cell(row, i + 1);
                    
                    if (val != null)
                    {
                        if (val is int || val is double || val is decimal || val is float)
                        {
                            cell.Value = Convert.ToDouble(val);
                        }
                        else if (val is DateTime dateTime)
                        {
                            cell.Value = dateTime;
                            cell.Style.DateFormat.Format = "yyyy-MM-dd HH:mm";
                        }
                        else
                        {
                            cell.Value = val.ToString();
                        }
                    }
                }
                row++;
            }

            worksheet.Columns().AdjustToContents();

            using var stream = new MemoryStream();
            workbook.SaveAs(stream);
            return stream.ToArray();
        }

        private string EscapeCsv(string field)
        {
            if (field.Contains(",") || field.Contains("\"") || field.Contains("\n") || field.Contains("\r"))
            {
                return $"\"{field.Replace("\"", "\"\"")}\"";
            }
            return field;
        }
    }
}
