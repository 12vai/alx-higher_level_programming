#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid Python list object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);

    // Additional information you want to print about the list elements
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid Python bytes object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first %ld bytes: ", size > 10 ? 10 : size);
    for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++) {
        printf("%02hhx", ((char *)PyBytes_AsString(p))[i]);
        if (i < (size > 10 ? 9 : size - 1)) {
            printf(" ");
        }
    }
    printf("\n");
}

// Example usage in main function
int main() {
    Py_Initialize();
    PyObject *my_list = PyList_New(0);
    PyObject *my_bytes = PyBytes_FromStringAndSize("Hello, world!", 13);

    print_python_list(my_list);
    print_python_bytes(my_bytes);

    Py_Finalize();
    return 0;
}
