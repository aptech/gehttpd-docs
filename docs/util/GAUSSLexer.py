# -*- coding: utf-8 -*-
"""
    pygments.lexers.gauss
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexers for GAUSS and related languages. Derived from C Lexer

    :copyright: Copyright 2006-2017 by the Pygments Team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import Lexer, RegexLexer, bygroups, words, do_insertions, \
    using, default, this, include
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Generic, Whitespace, Literal, Error


__all__ = ['GAUSSLexer']


class GAUSSLexer(RegexLexer):
    """
    For GAUSS source code.
    .. versionadded:: 0.10
    """
    name = 'GAUSS'
    aliases = ['gauss']
    filenames = ['*.e','*.gss','*.src']
    mimetypes = ['text/gauss']
    flags = re.M | re.I

    keyword = ("and", "bool", "break", "call", "callexe", "checkinterrupt", "clear", "clearg", "closeall", "cls", "comlog", "compile",
               "continue", "create", "debug", "declare", "delete", "disable", "dlibrary", "dllcall", "do", "dos", "edit", "ed", "else",
               "elseif", "enable", "end", "endfor", "endif", "endp", "endo", "errorlog", "errorlogat", "expr", "external", "fn",
               "format", "for", "goto", "gosub", "graph", "if", "keyword", "lib", "library", "library", "line", "load", "loadarray", "loadexe",
               "loadf", "loadk", "loadm", "loadp", "loads", "loadx", "locate", "loopnextindex", "lprint", "lpwidth", "lshow",
               "msym", "ndpclex", "new", "not", "open", "or", "output", "outwidth", "plotsym", "plot", "pop", "prcsn", "print",
               "printdos", "proc", "push", "retp", "return", "rndcon", "rndmod", "rndmult", "rndseed", "run", "saveall", "save", "screen",
               "scroll", "setarray", "show", "stop", "system", "trace", "trap", "threadfor", "threadendfor", "threadbegin", "threadjoin",
               "threadstat", "threadend", "until", "use", "while", "winprint", "with")

    declaration = ("struct", "local", "matrix", "string", "array", "scalar", "sparse", "let")

    built_in = ("abs", "acf", "aconcat", "aeye", "amax", "amean", "AmericanBinomCall", "AmericanBinomCall_Greeks", "AmericanBinomCall_ImpVol",
                "AmericanBinomPut", "AmericanBinomPut_Greeks", "AmericanBinomPut_ImpVol", "AmericanBSCall", "AmericanBSCall_Greeks",
                "AmericanBSCall_ImpVol", "AmericanBSPut", "AmericanBSPut_Greeks", "AmericanBSPut_ImpVol", "amin", "amult", "annotationGetDefaults",
                "annotationSetBkd", "annotationSetFont", "annotationSetLineColor", "annotationSetLineStyle", "annotationSetLineThickness",
                "annualTradingDays", "arccos", "arcsin", "areshape", "arrayalloc", "arrayindex", "arrayinit", "arraytomat", "asciiload", "asclabel", 
                "astd", "astds", "asum", "atan", "atan2", "atranspose", "axmargin", "balance", "band", "bandchol", "bandcholsol", "bandltsol", "bandrv",
                "bandsolpd", "bar", "base10", "begwind", "besselj", "bessely", "beta", "box", "boxcox", "cdfBeta", "cdfBetaInv", "cdfBinomial", 
                "cdfBinomialInv", "cdfBvn", "cdfBvn2", "cdfBvn2e", "cdfCauchy", "cdfCauchyInv", "cdfChic", "cdfChii", "cdfChinc", "cdfChincInv", "cdfExp",
                "cdfExpInv", "cdfFc", "cdfFnc", "cdfFncInv", "cdfGam", "cdfGenPareto", "cdfHyperGeo", "cdfLaplace", "cdfLaplaceInv", "cdfLogistic", 
                "cdfLogisticInv", "cdfmControlCreate", "cdfMvn", "cdfMvn2e", "cdfMvnce", "cdfMvne", "cdfMvt2e", "cdfMvtce", "cdfMvte", "cdfN", "cdfN2", 
                "cdfNc", "cdfNegBinomial", "cdfNegBinomialInv", "cdfNi", "cdfPoisson", "cdfPoissonInv", "cdfRayleigh", "cdfRayleighInv", "cdfTc", 
                "cdfTci", "cdfTnc", "cdfTvn", "cdfWeibull", "cdfWeibullInv", "cdir", "ceil", "ChangeDir", "chdir", "chiBarSquare", "chol", "choldn", 
                "cholsol", "cholup", "chrs", "close", "code", "cols", "colsf", "combinate", "combinated", "complex", "con", "cond", "conj", "cons", 
                "ConScore", "contour", "conv", "convertsatostr", "convertstrtosa", "corrm", "corrms", "corrvc", "corrx", "corrxs", "cos", "cosh", 
                "counts", "countwts", "crossprd", "crout", "croutp", "csrcol", "csrlin", "csvReadM", "csvReadSA", "cumprodc", "cumsumc", "curve", "cvtos",
                "datacreate", "datacreatecomplex", "datalist", "dataload", "dataloop", "dataopen", "datasave", "date", "datestr", "datestring", 
                "datestrymd", "dayinyr", "dayofweek", "dbAddDatabase", "dbClose", "dbCommit", "dbCreateQuery", "dbExecQuery", "dbGetConnectOptions", 
                "dbGetDatabaseName", "dbGetDriverName", "dbGetDrivers", "dbGetHostName", "dbGetLastErrorNum", "dbGetLastErrorText", 
                "dbGetNumericalPrecPolicy", "dbGetPassword", "dbGetPort", "dbGetTableHeaders", "dbGetTables", "dbGetUserName", "dbHasFeature", 
                "dbIsDriverAvailable", "dbIsOpen", "dbIsOpenError", "dbOpen", "dbQueryBindValue", "dbQueryClear", "dbQueryCols", "dbQueryExecPrepared", 
                "dbQueryFetchAllM", "dbQueryFetchAllSA", "dbQueryFetchOneM", "dbQueryFetchOneSA", "dbQueryFinish", "dbQueryGetBoundValue", 
                "dbQueryGetBoundValues", "dbQueryGetField", "dbQueryGetLastErrorNum", "dbQueryGetLastErrorText", "dbQueryGetLastInsertID", 
                "dbQueryGetLastQuery", "dbQueryGetPosition", "dbQueryIsActive", "dbQueryIsForwardOnly", "dbQueryIsNull", "dbQueryIsSelect", 
                "dbQueryIsValid", "dbQueryPrepare", "dbQueryRows", "dbQuerySeek", "dbQuerySeekFirst", "dbQuerySeekLast", "dbQuerySeekNext", 
                "dbQuerySeekPrevious", "dbQuerySetForwardOnly", "dbRemoveDatabase", "dbRollback", "dbSetConnectOptions", "dbSetDatabaseName", 
                "dbSetHostName", "dbSetNumericalPrecPolicy", "dbSetPort", "dbSetUserName", "dbTransaction", "DeleteFile", "delif", "delrows", 
                "denseToSp", "denseToSpRE", "denToZero", "design", "det", "detl", "dfft", "dffti", "diag", "diagrv", "digamma", "doswin", 
                "DOSWinCloseall", "DOSWinOpen", "dotfeq", "dotfeqmt", "dotfge", "dotfgemt", "dotfgt", "dotfgtmt", "dotfle", "dotflemt", "dotflt", 
                "dotfltmt", "dotfne", "dotfnemt", "draw", "drop", "dsCreate", "dstat", "dstatmt", "dstatmtControlCreate", "dtdate", "dtday", "dttime", 
                "dttodtv", "dttostr", "dttoutc", "dtvnormal", "dtvtodt", "dtvtoutc", "dummy", "dummybr", "dummydn", "eig", "eigh", "eighv", "eigv", 
                "elapsedTradingDays", "endwind", "envget", "eof", "eqSolve", "eqSolvemt", "eqSolvemtControlCreate", "eqSolvemtOutCreate", "eqSolveset", 
                "erf", "erfc", "erfccplx", "erfcplx", "error", "etdays", "ethsec", "etstr", "EuropeanBinomCall", "EuropeanBinomCall_Greeks", 
                "EuropeanBinomCall_ImpVol", "EuropeanBinomPut", "EuropeanBinomPut_Greeks", "EuropeanBinomPut_ImpVol", "EuropeanBSCall", 
                "EuropeanBSCall_Greeks", "EuropeanBSCall_ImpVol", "EuropeanBSPut", "EuropeanBSPut_Greeks", "EuropeanBSPut_ImpVol", "exctsmpl", "exec",
                "execbg", "exp", "extern", "eye", "fcheckerr", "fclearerr", "feq", "feqmt", "fflush", "fft", "ffti", "fftm", "fftmi", "fftn", "fge",
                "fgemt", "fgets", "fgetsa", "fgetsat", "fgetst", "fgt", "fgtmt", "fileinfo", "filesa", "fle", "flemt", "floor", "flt", "fltmt", "fmod",
                "fne", "fnemt", "fonts", "fopen", "formatcv", "formatnv", "fputs", "fputst", "fseek", "fstrerror", "ftell", "ftocv", "ftos", "ftostrC",
                "gamma", "gammacplx", "gammaii", "gausset", "gdaAppend", "gdaCreate", "gdaDStat", "gdaDStatMat", "gdaGetIndex", "gdaGetName", 
                "gdaGetNames", "gdaGetOrders", "gdaGetType", "gdaGetTypes", "gdaGetVarInfo", "gdaIsCplx", "gdaLoad", "gdaPack", "gdaRead", 
                "gdaReadByIndex", "gdaReadSome", "gdaReadSparse", "gdaReadStruct", "gdaReportVarInfo", "gdaSave", "gdaUpdate", "gdaUpdateAndPack", 
                "gdaVars", "gdaWrite", "gdaWrite32", "gdaWriteSome", "getarray", "getdims", "getf", "getGAUSShome", "getmatrix", "getmatrix4D", "getname",
                "getnamef", "getNextTradingDay", "getNextWeekDay", "getnr", "getorders", "getpath", "getPreviousTradingDay", "getPreviousWeekDay", 
                "getRow", "getscalar3D", "getscalar4D", "getTrRow", "getwind", "glm", "gradcplx", "gradMT", "gradMTm", "gradMTT", "gradMTTm", "gradp",
                "graphprt", "graphset", "hasimag", "header", "headermt", "hess", "hessMT", "hessMTg", "hessMTgw", "hessMTm", "hessMTmw", "hessMTT", 
                "hessMTTg", "hessMTTgw", "hessMTTm", "hessMTw", "hessp", "hist", "histf", "histp", "hsec", "imag", "indcv", "indexcat", "indices", 
                "indices2", "indicesf", "indicesfn", "indnv", "indsav", "indx", "integrate1d", "integrateControlCreate", "intgrat2", "intgrat3", "inthp1",
                "inthp2", "inthp3", "inthp4", "inthpControlCreate", "intquad1", "intquad2", "intquad3", "intrleav", "intrleavsa", "intrsect", "intsimp", 
                "inv", "invpd", "invswp", "iscplx", "iscplxf", "isden", "isinfnanmiss", "ismiss", "key", "keyav", "keyw", "lag", "lag1", "lagn", 
                "lapEighb", "lapEighi", "lapEighvb", "lapEighvi", "lapgEig", "lapgEigh", "lapgEighv", "lapgEigv", "lapgSchur", "lapgSvdcst", "lapgSvds", 
                "lapgSvdst", "lapSvdcusv", "lapSvds", "lapSvdusv", "ldlp", "ldlsol", "linSolve", "listwise", "ln", "lncdfbvn", "lncdfbvn2", "lncdfmvn", 
                "lncdfn", "lncdfn2", "lncdfnc", "lnfact", "lngammacplx", "lnpdfmvn", "lnpdfmvt", "lnpdfn", "lnpdft", "loadd", "loadstruct", "loadwind",
                "loess", "loessmt", "loessmtControlCreate", "log", "loglog", "logx", "logy", "lower", "lowmat", "lowmat1", "ltrisol", "lu", "lusol", 
                "machEpsilon", "make", "makevars", "makewind", "margin", "matalloc", "matinit", "mattoarray", "maxbytes", "maxc", "maxindc", "maxv", 
                "maxvec", "mbesselei", "mbesselei0", "mbesselei1", "mbesseli", "mbesseli0", "mbesseli1", "meanc", "median", "mergeby", "mergevar", "minc",
                "minindc", "minv", "miss", "missex", "missrv", "moment", "momentd", "movingave", "movingaveExpwgt", "movingaveWgt", "nextindex", "nextn", 
                "nextnevn", "nextwind", "ntos", "null", "null1", "numCombinations", "ols", "olsmt", "olsmtControlCreate", "olsqr", "olsqr2", "olsqrmt", 
                "ones", "optn", "optnevn", "orth", "outtyp", "pacf", "packedToSp", "packr", "parse", "pause", "pdfCauchy", "pdfChi", "pdfExp",
                "pdfGenPareto", "pdfHyperGeo", "pdfLaplace", "pdfLogistic", "pdfn", "pdfPoisson", "pdfRayleigh", "pdfWeibull", "pi", "pinv", "pinvmt", 
                "plotAddArrow", "plotAddBar", "plotAddBox", "plotAddHist", "plotAddHistF", "plotAddHistP", "plotAddPolar", "plotAddScatter", 
                "plotAddShape", "plotAddTextbox", "plotAddTS", "plotAddXY", "plotArea", "plotBar", "plotBox", "plotClearLayout", "plotContour", 
                "plotCustomLayout", "plotGetDefaults", "plotHist", "plotHistF", "plotHistP", "plotLayout", "plotLogLog", "plotLogX", "plotLogY", 
                "plotOpenWindow", "plotPolar", "plotSave", "plotScatter", "plotSetAxesPen", "plotSetBar", "plotSetBarFill", "plotSetBarStacked", 
                "plotSetBkdColor", "plotSetFill", "plotSetGrid", "plotSetLegend", "plotSetLineColor", "plotSetLineStyle", "plotSetLineSymbol",
                "plotSetLineThickness", "plotSetNewWindow", "plotSetTitle", "plotSetWhichYAxis", "plotSetXAxisShow", "plotSetXLabel", "plotSetXRange",
                "plotSetXTicInterval", "plotSetXTicLabel", "plotSetYAxisShow", "plotSetYLabel", "plotSetYRange", "plotSetZAxisShow", "plotSetZLabel",
                "plotSurface", "plotTS", "plotXY", "polar", "polychar", "polyeval", "polygamma", "polyint", "polymake", "polymat", "polymroot", 
                "polymult", "polyroot", "pqgwin", "previousindex", "princomp", "printfm", "printfmt", "prodc", "psi", "putarray", "putf", "putvals", 
                "pvCreate", "pvGetIndex", "pvGetParNames", "pvGetParVector", "pvLength", "pvList", "pvPack", "pvPacki", "pvPackm", "pvPackmi", "pvPacks",
                "pvPacksi", "pvPacksm", "pvPacksmi", "pvPutParVector", "pvTest", "pvUnpack", "QNewton", "QNewtonmt", "QNewtonmtControlCreate", 
                "QNewtonmtOutCreate", "QNewtonSet", "QProg", "QProgmt", "QProgmtInCreate", "qqr", "qqre", "qqrep", "qr", "qre", "qrep", "qrsol", 
                "qrtsol", "qtyr", "qtyre", "qtyrep", "quantile", "quantiled", "qyr", "qyre", "qyrep", "qz", "rank", "rankindx", "readr", "real", 
                "reclassify", "reclassifyCuts", "recode", "recserar", "recsercp", "recserrc", "rerun", "rescale", "reshape", "rets", "rev", "rfft",
                "rffti", "rfftip", "rfftn", "rfftnp", "rfftp", "rndBernoulli", "rndBeta", "rndBinomial", "rndCauchy", "rndChiSquare", "rndCon", 
                "rndCreateState", "rndExp", "rndGamma", "rndGeo", "rndGumbel", "rndHyperGeo", "rndi", "rndKMbeta", "rndKMgam", "rndKMi", "rndKMn", 
                "rndKMnb", "rndKMp", "rndKMu", "rndKMvm", "rndLaplace", "rndLCbeta", "rndLCgam", "rndLCi", "rndLCn", "rndLCnb", "rndLCp", "rndLCu", 
                "rndLCvm", "rndLogNorm", "rndMTu", "rndMVn", "rndMVt", "rndn", "rndnb", "rndNegBinomial", "rndp", "rndPoisson", "rndRayleigh",
                "rndStateSkip", "rndu", "rndvm", "rndWeibull", "rndWishart", "rotater", "round", "rows", "rowsf", "rref", "sampleData", "satostrC", 
                "saved", "saveStruct", "savewind", "scale", "scale3d", "scalerr", "scalinfnanmiss", "scalmiss", "schtoc", "schur", "searchsourcepath",
                "seekr", "select", "selif", "seqa", "seqm", "setdif", "setdifsa", "setvars", "setvwrmode", "setwind", "shell", "shiftr", "sin", 
                "singleindex", "sinh", "sleep", "solpd", "sortc", "sortcc", "sortd", "sorthc", "sorthcc", "sortind", "sortindc", "sortmc", "sortr",
                "sortrc", "spBiconjGradSol", "spChol", "spConjGradSol", "spCreate", "spDenseSubmat", "spDiagRvMat", "spEigv", "spEye", "spLDL",
                "spline", "spLU", "spNumNZE", "spOnes", "spreadSheetReadM", "spreadSheetReadSA", "spreadSheetWrite", "spScale", "spSubmat", "spToDense",
                "spTrTDense", "spTScalar", "spZeros", "sqpSolve", "sqpSolveMT", "sqpSolveMTControlCreate", "sqpSolveMTlagrangeCreate", 
                "sqpSolveMToutCreate", "sqpSolveSet", "sqrt", "statements", "stdc", "stdsc", "stocv", "stof", "strcombine", "strindx", "strlen", "strput",
                "strrindx", "strsect", "strsplit", "strsplitPad", "strtodt", "strtof", "strtofcplx", "strtriml", "strtrimr", "strtrim", "strtrunc",
                "strtruncl", "strtruncpad", "strtruncr", "submat", "subscat", "substute", "subvec", "sumc", "sumr", "surface", "svd", "svd1", "svd2",
                "svdcusv", "svds", "svdusv", "sysstate", "tab", "tan", "tanh", "tempname", "threadBegin", "threadEnd", "threadEndFor", "threadFor",
                "threadJoin", "threadStat", "time", "timedt", "timestr", "timeutc", "title", "tkf2eps", "tkf2ps", "tocart", "todaydt", "toeplitz",
                "token", "topolar", "trapchk", "trigamma", "trimr", "trunc", "type", "typecv", "typef", "union", "unionsa", "uniqindx", "uniqindxsa",
                "unique", "uniquesa", "upmat", "upmat1", "upper", "utctodt", "utctodtv", "utrisol", "vals", "varCovMS", "varCovXS", "varget", "vargetl",
                "varmall", "varmares", "varput", "varputl", "vartypef", "vcm", "vcms", "vcx", "vcxs", "vec", "vech", "vecr", "vector", "vget", "view",
                "viewxyz", "vlist", "vnamecv", "volume", "vput", "vread", "vtypecv", "wait", "waitc", "walkindex", "where", "window", "writer", "xlabel",
                "xlsGetSheetCount", "xlsGetSheetSize", "xlsGetSheetTypes", "xlsMakeRange", "xlsReadM", "xlsReadSA", "xlsWrite", "xlsWriteM",
                "xlsWriteSA", "xpnd", "xtics", "xy", "xyz", "ylabel", "ytics", "zeros", "zeta", "zlabel", "ztics")

    literal = ("DB_AFTER_LAST_ROW", "DB_ALL_TABLES", "DB_BATCH_OPERATIONS", "DB_BEFORE_FIRST_ROW", "DB_BLOB", "DB_EVENT_NOTIFICATIONS",
               "DB_FINISH_QUERY", "DB_HIGH_PRECISION", "DB_LAST_INSERT_ID", "DB_LOW_PRECISION_DOUBLE", "DB_LOW_PRECISION_INT32",
               "DB_LOW_PRECISION_INT64", "DB_LOW_PRECISION_NUMBERS", "DB_MULTIPLE_RESULT_SETS", "DB_NAMED_PLACEHOLDERS",
               "DB_POSITIONAL_PLACEHOLDERS", "DB_PREPARED_QUERIES", "DB_QUERY_SIZE", "DB_SIMPLE_LOCKING", "DB_SYSTEM_TABLES", "DB_TABLES",
               "DB_TRANSACTIONS", "DB_UNICODE", "DB_VIEWS", "__STDIN", "__STDOUT", "__STDERR")

    #: optional Comment or Whitespace
    _ws = r'(?:\s|//.*?\n|/[*].*?[*]/|@.*?@)+'

    # The trailing ?, rather than *, avoids a geometric performance drop here.
    #: only one /* */ style comment
    _ws1 = r'\s*(?:/[*].*?[*]/\s*|@.*?@\s*)?'

    _id_re = r'([a-zA-Z_]\w*)'

    tokens = {
        'whitespace': [
            # preprocessor directives: without whitespace
            ('^#if\s+0', Comment.Preproc, 'if0'),
            ('^#', Comment.Preproc, 'macro'),
            # or with whitespace
            ('^(' + _ws1 + r')(#if\s+0)',
             bygroups(using(this), Comment.Preproc), 'if0'),
            ('^(' + _ws1 + ')(#)',
             bygroups(using(this), Comment.Preproc), 'macro'),
            (r'\n', Text),
            (r'\s+', Text),
            (r'\\\n', Text),  # line continuation
            (r'//(\n|[\w\W]*?[^\\]\n)', Comment.Single),
            (r'/(\\\n)?[*][\w\W]*?[*](\\\n)?/', Comment.Multiline),
            (r'@[\w\W]*?@', Comment.Multiline),
            # Open until EOF, so no ending delimeter
            (r'/(\\\n)?[*][\w\W]*', Comment.Multiline),
        ],
        'statements': [
            (r'"', String, 'string'),
            (r'0x[0-9a-fA-F]+', Number.Hex),
            (r'(\d+\.\d*|\.\d+|\d+)[eE][+-]?\d+', Number.Float),
            (r'(-?)((\b\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?)', Number.Float),
            (r'\d+[eE][+-]?[0-9]+', Number.Float),
            (r'\d+', Number.Integer),
            (r'\*/', Error),
            (r'\.?\$?(?:\.?[ngl]e\b|\.?[gl]t\b)', Operator.Word),
            (r'\.?(?:and|x?or|not|eqv?)\b', Operator.Word),
            (r'\.?\$?(?:[~\/=!]=|[<>]=?)|%|\$?[\|+\-~]', Operator),
            (r'\.?\*\.?|[+\/!\|]|\.?[\/^\']|\*?~|&|\$', Operator),
            (r'\[|\]|\(|\)|\{|\}|\.|,|=|\?|:|;', Punctuation),
            (r'(struct)(\s+)' + _id_re, bygroups(Keyword, Whitespace, Name.Class)),
            (r'(?:(for|threadfor)\b)(\s*)' + _id_re, bygroups(Keyword, Whitespace, Name)), # special 'for' case
            (r'(fn)(\s+)' + _id_re + r'([^=]*?)(=)', bygroups(Keyword, Whitespace, Name.Function, using(this), Punctuation)),
            (words(literal, suffix=r'\b'), Literal),
            (words(keyword, suffix=r'\b'), Keyword),
            #(words(built_in, suffix=r'\b'), Name.Function),
            (words(declaration, suffix=r'\b'), Keyword.Declaration),
            (_id_re + r'(\s*)(\()', bygroups(Name.Function, Whitespace, Punctuation)),
            (r'(^\s*)' + _id_re + r'(:)(?!:)', bygroups(Whitespace, Name.Label, Punctuation)),
            (_id_re + r'(\.|->)' + _id_re, bygroups(Name, Punctuation, Name.Attribute), 'structmember'),
            (_id_re, Name),
        ],
        'structmember': [
            (r'(\.)' + _id_re, bygroups(Punctuation, Name.Attribute)),
            default('#pop'),
        ],
        'root': [
            include('whitespace'),
            include('statement'),
            (r'.', Text),
        ],
        'statement': [
            include('whitespace'),
            include('statements'),
            #(';', Punctuation, '#pop'),
        ],
        'string': [
            (r'"', String, '#pop'),
            (r'\\([\\abfnrtv"\']|x[a-fA-F0-9]{2,4}|'
             r'u[a-fA-F0-9]{4}|U[a-fA-F0-9]{8}|[0-7]{1,3})', String.Escape),
            (r'[^\\"]+', String),  # all other characters
            (r'\\\n', String),  # line continuation
            (r'\\', String),  # stray backslash
        ],
        'macro': [
            (r'(include)(' + _ws1 + r')([^\n]+)',
             bygroups(Comment.Preproc, Text, Comment.PreprocFile)),
            (r'[^/\n]+', Comment.Preproc),
            (r'/[*](.|\n)*?[*]/', Comment.Multiline),
            (r'@(.|\n)*?@', Comment.Multiline),
            (r'//.*?\n', Comment.Single, '#pop'),
            (r'/', Comment.Preproc),
            (r'(?<=\\)\n', Comment.Preproc),
            (r'\n', Comment.Preproc, '#pop'),
        ],
        'if0': [
            (r'^\s*#if.*?(?<!\\)\n', Comment.Preproc, '#push'),
            (r'^\s*#el(?:se|if).*\n', Comment.Preproc, '#pop'),
            (r'^\s*#endif.*?(?<!\\)\n', Comment.Preproc, '#pop'),
            (r'.*?\n', Comment),
        ],
    }

    def analyse_text(text):
        if re.search('^\s*(?:endp|endfor)\s*;', text, re.MULTILINE): # end of proc
            return 0.2
        elif re.search('^\s*proc ', text, re.MULTILINE):  # system cmd
            return 0.2


