#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
*print_python_list - prints basic python list info
*@p: pyObject list
*Return: Nothing.
*/
void print_python_list(PyObject *p):
{
Py_ssize_t size, alloc, i;
const char *type;
PyListObject *list = (PyListObject *)p;
PyVarObject *var = (PyVarObject *)p;
size = var->ob_size;
alloc = list->allocated;
type = var->ob_type->tp_name;
printf("%s size: %zd, alloc: %zd\n", type, size, alloc);
for (i = 0; i < size; i++)
{
printf("[%d] ", i);
print_python_object(list->ob_item[i]);
}
}
/**
*print_python_bytes - prints basic python bytes info
*@p: pyObject bytes
*Return: Nothing.
*/
void print_python_bytes(PyObject *p):
{
Py_ssize_t size, alloc, i;
const char *type;
PyBytesObject *bytes = (PyBytesObject *)p;
PyVarObject *var = (PyVarObject *)p;
size = var->ob_size;
alloc = bytes->ob_alloc;
type = var->ob_type->tp_name;
printf("%s size: %zd, alloc: %zd\n", type, size, alloc);
for (i = 0; i < size; i++)
{
printf("[%d] ", i);
printf("%c", bytes->ob_sval[i]);
}
}
/**
*print_python_float - prints basic python float info
*@p: pyObject float
*Return: Nothing.
*/
void print_python_float(PyObject *p):
{
Py_ssize_t size, alloc, i;
const char *type;
PyFloatObject *float_obj = (PyFloatObject *)p;
PyVarObject *var = (PyVarObject *)p;
size = var->ob_size;
alloc = float_obj->ob_alloc;
type = var->ob_type->tp_name;
printf("%s size: %zd, alloc: %zd\n", type, size, alloc);
for (i = 0; i < size; i++)
{
printf("[%d] ", i);
printf("%f", float_obj->ob_fval);
}
}
