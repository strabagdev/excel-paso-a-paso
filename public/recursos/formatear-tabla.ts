function main(workbook: ExcelScript.Workbook): number {
  const tabla = workbook.getTable("Actividades");
  if (!tabla) throw new Error("Falta la tabla Actividades");
  tabla.getRange().getFormat().autofitColumns();
  return tabla.getRowCount();
}
