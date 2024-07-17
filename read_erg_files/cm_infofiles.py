# encoding: utf-8

#  Copyright (c) 2019:      IPG Automotive GmbH
#  Bannwaldallee 60         Phone  +49.721.98520.0
#  76185 Karlsruhe          Fax    +49.721.98520.99
#  Germany                  www    www.ipg-automotive.com
#  last author: dak

# module cm_infofiles
# from C:/Users/giri.aigalikar/Documents/Erg_Python/read_erg_files/utility/cm_infofiles.pyd
# by generator 1.147
""" A python wrapper for CarMaker InfoFile modification. """

# imports
import Boost.Python as __Boost_Python


# no functions
# classes

# noinspection PyRedeclaration,PyMissingOrEmptyDocstring
class DoubleTable(__Boost_Python.instance):
    # no doc
    def append(self, new_line):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        append( (DoubleTable)arg1, (object)arg2) -> None :
        
            C++ signature :
                void append(cmlib::InfoFileTable<double> {lvalue},boost::python::api::object)
        """
        pass

    def extend(self, list_new_lines):  # real signature unknown; NOTE: unreliably
        # restored from __doc__
        """
        extend( (DoubleTable)arg1, (object)arg2) -> None :
        
            C++ signature :
                void extend(cmlib::InfoFileTable<double> {lvalue},boost::python::api::object)
        """
        pass

    def __contains__(self, check_for_item):  # real signature unknown; NOTE: unreliably restored
        # from __doc__
        """
        __contains__( (DoubleTable)arg1, (object)arg2) -> bool :
        
            C++ signature :
                bool __contains__(cmlib::InfoFileTable<double> {lvalue},_object*)
        """
        pass

    def __delitem__(self, delete_pos):  # real signature unknown; NOTE: unreliably restored from
        # __doc__
        """
        __delitem__( (DoubleTable)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __delitem__(cmlib::InfoFileTable<double> {lvalue},_object*)
        """
        pass

    def __getitem__(self, item_pos):  # real signature unknown; NOTE: unreliably restored from
        # __doc__
        """
        __getitem__( (object)arg1, (object)arg2) -> object :
        
            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<cmlib::InfoFileTable<double>&>,_object*)
        """
        pass

    def __init__(self, dim_1, dim_2):  # real signature unknown; NOTE: unreliably restored from
        # __doc__
        """
        __init__( (object)arg1, (int)arg2, (int)arg3) -> None :
        
            C++ signature :
                void __init__(_object*,unsigned long,unsigned long)
        
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        
        __init__( (object)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __init__(_object*,std::vector<std::vector<double, std::allocator<double> >, std::allocator<std::vector<double, std::allocator<double> > > >)
        """
        pass

    def __init__(self):
        pass

    def __init__(self, list):
        pass

    def __init__(self, other):
        pass

    def __iter__(self, p_object, *args,
                 **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_internal_reference<1ul, boost::python::default_call_policies>, __gnu_cxx::__normal_iterator<std::vector<double, std::allocator<double> >*, std::vector<std::vector<double, std::allocator<double> >, std::allocator<std::vector<double, std::allocator<double> > > > > > __iter__(boost::python::back_reference<cmlib::InfoFileTable<double>&>)
        """
        pass

    def __len__(self, DoubleTable, *args,
                **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __len__( (DoubleTable)arg1) -> int :
        
            C++ signature :
                unsigned long __len__(cmlib::InfoFileTable<double> {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        pass

    def __setitem__(self, DoubleTable, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __setitem__( (DoubleTable)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void __setitem__(cmlib::InfoFileTable<double> {lvalue},_object*,_object*)
        """
        pass

    def __str__(self, DoubleTable, *args,
                **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __str__( (DoubleTable)arg1) -> str :
        
            C++ signature :
                std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > __str__(cmlib::InfoFileTable<double> {lvalue})
        """
        pass

    __instance_size__ = 40


class DoubleVector(__Boost_Python.instance):
    # no doc
    def append(self, value):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        append( (DoubleVector)arg1, (object)arg2) -> None :
        
            C++ signature :
                void append(std::vector<double, std::allocator<double> > {lvalue},boost::python::api::object)
        """
        pass

    def extend(self, list_values):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        extend( (DoubleVector)arg1, (object)arg2) -> None :
        
            C++ signature :
                void extend(std::vector<double, std::allocator<double> > {lvalue},boost::python::api::object)
        """
        pass

    def __contains__(self, check_for):  # real signature unknown; NOTE: unreliably restored from
        # __doc__
        """
        __contains__( (DoubleVector)arg1, (object)arg2) -> bool :
        
            C++ signature :
                bool __contains__(std::vector<double, std::allocator<double> > {lvalue},_object*)
        """
        pass

    def __delitem__(self, DoubleVector, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __delitem__( (DoubleVector)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __delitem__(std::vector<double, std::allocator<double> > {lvalue},_object*)
        """
        pass

    def __getitem__(self, p_object, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __getitem__( (object)arg1, (object)arg2) -> object :
        
            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<std::vector<double, std::allocator<double> >&>,_object*)
        """
        pass

    def __init__(self, p_object, *args,
                 **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        
        __init__( (object)arg1, (DoubleVector)arg2) -> None :
        
            C++ signature :
                void __init__(_object*,std::vector<double, std::allocator<double> >)
        """
        pass

    def __init__(self):
        pass

    def __init__(self, double_list):
        pass

    def __iter__(self, p_object, *args,
                 **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_value_policy<boost::python::return_by_value, boost::python::default_call_policies>, __gnu_cxx::__normal_iterator<double*, std::vector<double, std::allocator<double> > > > __iter__(boost::python::back_reference<std::vector<double, std::allocator<double> >&>)
        """
        pass

    def __len__(self, DoubleVector, *args,
                **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __len__( (DoubleVector)arg1) -> int :
        
            C++ signature :
                unsigned long __len__(std::vector<double, std::allocator<double> > {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        pass

    def __setitem__(self, DoubleVector, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __setitem__( (DoubleVector)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void __setitem__(std::vector<double, std::allocator<double> > {lvalue},_object*,_object*)
        """
        pass

    def __str__(self, DoubleVector, *args,
                **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __str__( (DoubleVector)arg1) -> str :
        
            C++ signature :
                std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > __str__(std::vector<double, std::allocator<double> >)
        """
        pass

    __instance_size__ = 40


class InfoFile(__Boost_Python.instance):
    """ A CarMaker InfoFile object that supports I/O to files. """

    def add_comment_line_before(self, key_name, str_comment):  # real signature unknown; NOTE:
        # unreliably restored
        # from __doc__
        """
        add_comment_line_before( (InfoFile)arg1, (str)arg2, (str)key_name) -> None :
            Add a comment line (text only) before the line identified by key_name
        
            C++ signature :
                void add_comment_line_before(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def add_line_behind(self, key_name, str_comment):  # real signature unknown; NOTE: unreliably
        # restored from
        # __doc__
        """
        add_line_behind( (InfoFile)arg1, (str)arg2, (str)key_name) -> None :
            Add a comment line (text only) behind the line identified by key_name
        
            C++ signature :
                void add_line_behind(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def key_exists(self, key_name):
        """
        key_exists( (InfoFile)arg1, (str)key_name) -> bool :
            Check whether a given key exists.

            C++ signature :
                bool key_exists(cmlib::InfoFileBase {lvalue}, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def del_key(self, key_name):  # real signature unknown; NOTE: unreliably restored from
        # __doc__
        """
        del_key( (InfoFile)arg1, (str)key_name) -> None :
            Deletes the key with the given name.
        
            C++ signature :
                void del_key(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def get_double(self, key_name):  # real signature unknown; NOTE: unreliably restored from
        # __doc__
        """
        get_double( (InfoFile)arg1, (str)key_name) -> float :
            Get the given key as a double value
        
            C++ signature :
                double get_double(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def get_double_or_default(self, key_name, default_val):  # real signature unknown; NOTE:
        # unreliably restored from __doc__
        """
        get_double_or_default( (InfoFile)arg1, (str)arg2, (float)key_name) -> float :
            Get the given key as a double value or the specified default if it is not set
        
            C++ signature :
                double get_double_or_default(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,double)
        """
        pass

    def get_double_table(self, key_name):  # real signature unknown; NOTE: unreliably
        # restored from __doc__
        """
        get_double_table( (InfoFile)arg1, (str)key_name) -> DoubleTable :
            Get the given key as a double table
        
            C++ signature :
                cmlib::InfoFileTable<double> get_double_table(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def get_double_vector(self, key_name):  # real signature unknown; NOTE: unreliably
        # restored
        # from __doc__
        """
        get_double_table( (InfoFile)arg1, (str)key_name) -> doubleVector :
            Get the given key as an double vector
        
            C++ signature :
                std::vector<double> get_double_table(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def get_int(self, key_name):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        get_int( (InfoFile)arg1, (str)key_name) -> int :
            Get the given key as a int value
        
            C++ signature :
                int get_int(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def get_int_or_default(self, key_name, def_value):  # real signature unknown; NOTE: unreliably
        # restored from __doc__
        """
        get_int_or_default( (InfoFile)arg1, (str)arg2, (int)key_name) -> int :
            Get the given key as a int value or the specified default if it is not set
        
            C++ signature :
                int get_int_or_default(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,int)
        """
        pass

    def get_int_table(self, key_name):  # real signature unknown; NOTE: unreliably
        # restored
        # from __doc__
        """
        get_int_table( (InfoFile)arg1, (str)key_name) -> IntTable :
            Get the given key as an int table
        
            C++ signature :
                cmlib::InfoFileTable<int> get_int_table(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def get_int_vector(self, key_name):  # real signature unknown; NOTE: unreliably
        # restored
        # from __doc__
        """
        get_int_table( (InfoFile)arg1, (str)key_name) -> IntVector :
            Get the given key as an int vector
        
            C++ signature :
                std::vector<int> get_int_table(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass


    def get_string(self, key_name):  # real signature unknown; NOTE: unreliably restored from
        # __doc__
        """
        get_string( (InfoFile)arg1, (str)key_name) -> str :
            Get the given key as a string
        
            C++ signature :
                std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > get_string(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def get_string_or_default(self, key_name, default_str):  # real signature unknown; NOTE:
        # unreliably restored from __doc__
        """
        get_string_or_default( (InfoFile)arg1, (str)arg2, (str)key_name) -> str :
            Get the given key as a string or the specified default if it is not set
        
            C++ signature :
                std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > get_string_or_default(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def get_string_table(self, key_name):  # real signature unknown; NOTE: unreliably restored from
        # __doc__
        """
        get_string_table( (InfoFile)arg1, (str)key_name) -> StrTable :
            Get the given key as a string table
        
            C++ signature :
                cmlib::InfoFileTable<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > get_string_table(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def get_string_vector(self, key_name):  # real signature unknown; NOTE: unreliably
        # restored
        # from __doc__
        """
        get_string_table( (InfoFile)arg1, (str)key_name) -> StringVector :
            Get the given key as an string vector
        
            C++ signature :
                std::vector<std::string> get_string_table(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def list_keys(self, prefix, list_key_type=List_types.all_keys):  # real signature unknown; NOTE:
        # unreliably
        # restored
        # from __doc__
        """
        list_keys( (InfoFile)arg1, (str)key_name [, (List_types)list_type]) -> StringVector :
            List all keys under the given key_name
        
            C++ signature :
                std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > list_keys(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > [,cmlib::InfoFileBase::e_key_list_what])
        """
        pass

    def read(self, str_file_path):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        read( (InfoFile)arg1, (str)fname) -> None :
            Reads the Infofile from the given fname into this object
        
            C++ signature :
                void read(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def set_double(self, key_name, value):  # real signature unknown; NOTE: unreliably restored from
        # __doc__
        """
        set_double( (InfoFile)arg1, (str)arg2, (float)key_name) -> None :
            Set the given key to the given double value
        
            C++ signature :
                void set_double(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,double)
        """
        pass

    def set_double_vector(self, key_name,
                          list_values):  # real signature unknown; NOTE: unreliably restored from
        # __doc__
        """
        set_double( (InfoFile)arg1, (string)key_name, (list)list_values) -> None :
            Set the given key to the given list of doubles.
        
            C++ signature :
                void set_double_vector(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::vector<double>)
        """
        pass

    def set_double_table(self, key_name, table):  # real signature unknown; NOTE: unreliably
        # restored from __doc__
        """
        set_double_table( (InfoFile)arg1, (str)arg2, (DoubleTable)key_name) -> None :
            Set the given key to the given table
        
            C++ signature :
                void set_double_table(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,cmlib::InfoFileTable<double>)
        """
        pass

    def set_int(self, key_name, value):  # real signature unknown; NOTE: unreliably restored from
        # __doc__
        """
        set_int( (InfoFile)arg1, (str)arg2, (int)key_name) -> None :
            Set the given key to the given int value
        
            C++ signature :
                void set_int(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,int)
        """
        pass

    def set_int_table(self, key_name, table):  # real signature unknown; NOTE: unreliably restored
        # from __doc__
        """
        set_int_table( (InfoFile)arg1, (str)arg2, (IntTable)key_name) -> None :
            Set the given key to the given table
        
            C++ signature :
                void set_int_table(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,cmlib::InfoFileTable<int>)
        """
        pass

    def set_int_vector(self, key_name,
                       list_values):  # real signature unknown; NOTE: unreliably restored from
        # __doc__
        """
        set_int_vector( (InfoFile)arg1, (string)key_name, (list)list_values) -> None :
            Set the given key to the given list of ints.
        
            C++ signature :
                void set_int_vector(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::vector<int>)
        """
        pass

    def set_string(self, key_name, value):  # real signature unknown; NOTE: unreliably restored from
        # alue# __doc__
        """
        set_string( (InfoFile)arg1, (str)arg2, (str)key_name) -> None :
            Set the given key to the given string
        
            C++ signature :
                void set_string(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def set_string_table(self, key_name, value):  # real signature unknown; NOTE: unreliably
        # restored from __doc__
        """
        set_string_table( (InfoFile)arg1, (str)arg2, (StrTable)key_name) -> None :
            Set the given key to the given table
        
            C++ signature :
                void set_string_table(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,cmlib::InfoFileTable<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >)
        """
        pass

    def set_string_vector(self, key_name,
                          list_values):  # real signature unknown; NOTE: unreliably restored from
        # __doc__
        """
        set_string_vector( (InfoFile)arg1, (string)key_name, (list)list_values) -> None :
            Set the given key to the given list of strings.
        
            C++ signature :
                void set_string_vector(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >,std::vector<std::string>)
        """
        pass

    def write(self, fname):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        write( (InfoFile)arg1, (str)fname) -> None :
            Write the Infofile from this object to given fname.
        
            C++ signature :
                void write(cmlib::InfoFileBase {lvalue},std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def __init__(self, p_object, *args,
                 **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        
        __init__( (object)self) -> None :
            Construct an empty Info file.
        
            C++ signature :
                void __init__(_object*)
        
        __init__( (object)arg1, (str)fname) -> None :
            Construct an Info file by reading in the file with the given fname.
        
            C++ signature :
                void __init__(_object*,std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >)
        """
        pass

    def __init__(self, fname):
        pass

    def __init__(self):
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        pass

    __instance_size__ = 40


class IntTable(__Boost_Python.instance):
    # no doc
    def append(self, new_line):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        append( (IntTable)arg1, (object)arg2) -> None :
        
            C++ signature :
                void append(cmlib::InfoFileTable<int> {lvalue},boost::python::api::object)
        """
        pass

    def extend(self, list_new_lines):  # real signature unknown; NOTE: unreliably
        """
        extend( (IntTable)arg1, (object)arg2) -> None :

            C++ signature :
                void extend(cmlib::InfoFileTable<int> {lvalue},boost::python::api::object)
        """
        pass

    def __contains__(self, check_for_item):  # real signature unknown; NOTE: unreliably restored
        """
        __contains__( (IntTable)arg1, (object)arg2) -> bool :

            C++ signature :
                bool __contains__(cmlib::InfoFileTable<int> {lvalue},_object*)
        """
        pass

    def __delitem__(self, IntTable, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __delitem__( (IntTable)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __delitem__(cmlib::InfoFileTable<int> {lvalue},_object*)
        """
        pass

    def __getitem__(self, p_object, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __getitem__( (object)arg1, (object)arg2) -> object :
        
            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<cmlib::InfoFileTable<int>&>,_object*)
        """
        pass

    def __init__(self, p_object, *args,
                 **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __init__( (object)arg1, (int)arg2, (int)arg3) -> None :
        
            C++ signature :
                void __init__(_object*,unsigned long,unsigned long)
        
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        
        __init__( (object)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __init__(_object*,std::vector<std::vector<int, std::allocator<int> >, std::allocator<std::vector<int, std::allocator<int> > > >)
        """
        pass

    def __init__(self):
        pass

    def __init__(self, list):
        pass

    def __init__(self, other):
        pass

    def __iter__(self, p_object, *args,
                 **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_internal_reference<1ul, boost::python::default_call_policies>, __gnu_cxx::__normal_iterator<std::vector<int, std::allocator<int> >*, std::vector<std::vector<int, std::allocator<int> >, std::allocator<std::vector<int, std::allocator<int> > > > > > __iter__(boost::python::back_reference<cmlib::InfoFileTable<int>&>)
        """
        pass

    def __len__(self, IntTable, *args,
                **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __len__( (IntTable)arg1) -> int :
        
            C++ signature :
                unsigned long __len__(cmlib::InfoFileTable<int> {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        pass

    def __setitem__(self, IntTable, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __setitem__( (IntTable)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void __setitem__(cmlib::InfoFileTable<int> {lvalue},_object*,_object*)
        """
        pass

    def __str__(self, IntTable, *args,
                **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __str__( (IntTable)arg1) -> str :
        
            C++ signature :
                std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > __str__(cmlib::InfoFileTable<int> {lvalue})
        """
        pass

    __instance_size__ = 40


class IntVector(__Boost_Python.instance):
    # no doc
    def append(self, value):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        append( (IntVector)arg1, (object)arg2) -> None :
        
            C++ signature :
                void append(std::vector<int, std::allocator<int> > {lvalue},boost::python::api::object)
        """
        pass

    def extend(self, list_values):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        extend( (IntVector)arg1, (object)arg2) -> None :
        
            C++ signature :
                void extend(std::vector<int, std::allocator<int> > {lvalue},boost::python::api::object)
        """
        pass

    def __contains__(self, check_for):  # real signature unknown; NOTE: unreliably restored from
        """
        __contains__( (IntVector)arg1, (object)arg2) -> bool :
        
            C++ signature :
                bool __contains__(std::vector<int, std::allocator<int> > {lvalue},_object*)
        """
        pass

    def __delitem__(self, IntVector, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __delitem__( (IntVector)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __delitem__(std::vector<int, std::allocator<int> > {lvalue},_object*)
        """
        pass

    def __getitem__(self, p_object, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __getitem__( (object)arg1, (object)arg2) -> object :
        
            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<std::vector<int, std::allocator<int> >&>,_object*)
        """
        pass

    def __init__(self, p_object, *args,
                 **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        
        __init__( (object)arg1, (IntVector)arg2) -> None :
        
            C++ signature :
                void __init__(_object*,std::vector<int, std::allocator<int> >)
        """
        pass

    def __init__(self):
        pass

    def __init__(self, int_list):
        pass

    def __iter__(self, p_object, *args,
                 **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_value_policy<boost::python::return_by_value, boost::python::default_call_policies>, __gnu_cxx::__normal_iterator<int*, std::vector<int, std::allocator<int> > > > __iter__(boost::python::back_reference<std::vector<int, std::allocator<int> >&>)
        """
        pass

    def __len__(self, IntVector, *args,
                **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __len__( (IntVector)arg1) -> int :
        
            C++ signature :
                unsigned long __len__(std::vector<int, std::allocator<int> > {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        pass

    def __setitem__(self, IntVector, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __setitem__( (IntVector)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void __setitem__(std::vector<int, std::allocator<int> > {lvalue},_object*,_object*)
        """
        pass

    def __str__(self, IntVector, *args,
                **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __str__( (IntVector)arg1) -> str :
        
            C++ signature :
                std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > __str__(std::vector<int, std::allocator<int> >)
        """
        pass

    __instance_size__ = 40


class List_types(__Boost_Python.enum):
    # no doc
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    all_keys = 3
    names = {
        'all_keys'   : 3,
        'one_level'  : 0,
        'sub_keys'   : 1,
        'unread_keys': 2,
    }
    one_level = 0
    sub_keys = 1
    unread_keys = 2
    values = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }
    __slots__ = ()


class StringVector(__Boost_Python.instance):
    # no doc
    def append(self, value):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        append( (StringVector)arg1, (object)arg2) -> None :
        
            C++ signature :
                void append(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > {lvalue},boost::python::api::object)
        """
        pass

    def extend(self, list_values):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        extend( (StringVector)arg1, (object)arg2) -> None :
        
            C++ signature :
                void extend(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > {lvalue},boost::python::api::object)
        """
        pass

    def __contains__(self, check_for):  # real signature unknown; NOTE: unreliably restored from
        """
        __contains__( (StringVector)arg1, (object)arg2) -> bool :
        
            C++ signature :
                bool __contains__(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > {lvalue},_object*)
        """
        pass

    def __delitem__(self, StringVector, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __delitem__( (StringVector)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __delitem__(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > {lvalue},_object*)
        """
        pass

    def __getitem__(self, p_object, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __getitem__( (object)arg1, (object)arg2) -> object :
        
            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&>,_object*)
        """
        pass

    def __init__(self, p_object, *args,
                 **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        
        __init__( (object)arg1, (StringVector)arg2) -> None :
        
            C++ signature :
                void __init__(_object*,std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >)
        """
        pass

    def __init__(self):
        pass

    def __init__(self, string_list):
        pass

    def __iter__(self, p_object, *args,
                 **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_value_policy<boost::python::return_by_value, boost::python::default_call_policies>, __gnu_cxx::__normal_iterator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > > __iter__(boost::python::back_reference<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >&>)
        """
        pass

    def __len__(self, StringVector, *args,
                **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __len__( (StringVector)arg1) -> int :
        
            C++ signature :
                unsigned long __len__(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        pass

    def __setitem__(self, StringVector, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __setitem__( (StringVector)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void __setitem__(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > {lvalue},_object*,_object*)
        """
        pass

    def __str__(self, StringVector, *args,
                **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __str__( (StringVector)arg1) -> str :
        
            C++ signature :
                std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > __str__(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >)
        """
        pass

    __instance_size__ = 40


class StringTable(__Boost_Python.instance):
    # no doc
    def append(self, new_line):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        append( (StrTable)arg1, (object)arg2) -> None :
        
            C++ signature :
                void append(cmlib::InfoFileTable<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > {lvalue},boost::python::api::object)
        """
        pass

    def extend(self, list_new_lines):  # real signature unknown; NOTE: unreliably
        """
        extend( (StrTable)arg1, (object)arg2) -> None :
        
            C++ signature :
                void extend(cmlib::InfoFileTable<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > {lvalue},boost::python::api::object)
        """
        pass

    def __contains__(self, check_for_item):  # real signature unknown; NOTE: unreliably restored
        """
        __contains__( (StrTable)arg1, (object)arg2) -> bool :
        
            C++ signature :
                bool __contains__(cmlib::InfoFileTable<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > {lvalue},_object*)
        """
        pass

    def __delitem__(self, StrTable, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __delitem__( (StrTable)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __delitem__(cmlib::InfoFileTable<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > {lvalue},_object*)
        """
        pass

    def __getitem__(self, p_object, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __getitem__( (object)arg1, (object)arg2) -> object :
        
            C++ signature :
                boost::python::api::object __getitem__(boost::python::back_reference<cmlib::InfoFileTable<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&>,_object*)
        """
        pass

    def __init__(self, p_object, *args,
                 **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __init__( (object)arg1, (int)arg2, (int)arg3) -> None :
        
            C++ signature :
                void __init__(_object*,unsigned long,unsigned long)
        
        __init__( (object)arg1) -> None :
        
            C++ signature :
                void __init__(_object*)
        
        __init__( (object)arg1, (object)arg2) -> None :
        
            C++ signature :
                void __init__(_object*,std::vector<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >, std::allocator<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >)
        """
        pass

    def __init__(self):
        pass

    def __init__(self, list):
        pass

    def __init__(self, other):
        pass

    def __iter__(self, p_object, *args,
                 **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __iter__( (object)arg1) -> object :
        
            C++ signature :
                boost::python::objects::iterator_range<boost::python::return_internal_reference<1ul, boost::python::default_call_policies>, __gnu_cxx::__normal_iterator<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >*, std::vector<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >, std::allocator<std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > > > > __iter__(boost::python::back_reference<cmlib::InfoFileTable<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&>)
        """
        pass

    def __len__(self, StrTable, *args,
                **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __len__( (StrTable)arg1) -> int :
        
            C++ signature :
                unsigned long __len__(cmlib::InfoFileTable<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > {lvalue})
        """
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        pass

    def __setitem__(self, StrTable, *args,
                    **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __setitem__( (StrTable)arg1, (object)arg2, (object)arg3) -> None :
        
            C++ signature :
                void __setitem__(cmlib::InfoFileTable<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > {lvalue},_object*,_object*)
        """
        pass

    def __str__(self, StrTable, *args,
                **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        __str__( (StrTable)arg1) -> str :
        
            C++ signature :
                std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > __str__(cmlib::InfoFileTable<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > {lvalue})
        """
        pass

    __instance_size__ = 40


# variables with complex values

__loader__ = None  # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc389d86da0>'

__spec__ = None  # (!) real value is "ModuleSpec(name='cm_infofiles', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fc389d86da0>, origin='/fs/u5/Projects/Hyundai/200754_HMC_Anchor/CM_Projects/Software/master/utility/cm_infofiles.so')"
