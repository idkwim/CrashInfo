from NTSTATUS import *;

# Used for consistency

ddtxExceptionTranslation_xExceptionCodeOrTypeId = {
  "AVW:NULL": {
    "Assert": (
      "The process caused an access violation by writing to NULL to indicate an assertion failed",
      "This is probably not a security isssue",
      [
        [
          "mozglue.dll!mozalloc_abort",
          "xul.dll!NS_DebugBreak",
        ],
      ],
    ),
    "OOM": (
      "The process caused an access violation by writing to NULL to indicate it was unable to allocate enough memory",
      None,
      [
        [
          "chrome.dll!CrashOnProcessDetach",
          "chrome.dll!DllMain",
          "chrome.dll!__DllMainCRTStartup",
          "chrome.dll!_DllMainCRTStartup",
          "ntdll.dll!LdrpCallInitRoutine",
          "ntdll.dll!LdrShutdownProcess",
          "ntdll.dll!RtlExitUserProcess",
          "kernel32.dll!ExitProcessStub",
          "chrome.dll!__crtExitProcess",
          "chrome.dll!doexit",
          "chrome.dll!_exit",
          "chrome.dll!base::`anonymous namespace'::OnNoMemory",
        ], [
          "chrome.dll!CrashOnProcessDetach",
          "chrome.dll!DllMain",
          "chrome.dll!__DllMainCRTStartup",
          "chrome.dll!_DllMainCRTStartup",
          "ntdll.dll!LdrxCallInitRoutine", # different from the above stack here
          "ntdll.dll!LdrpCallInitRoutine", # and here
          "ntdll.dll!LdrShutdownProcess",
          "ntdll.dll!RtlExitUserProcess",
          "KERNEL32.DLL!ExitProcessImplementation",# and here
          "chrome.dll!__crtExitProcess",
          "chrome.dll!doexit",
          "chrome.dll!_exit",
          "chrome.dll!base::`anonymous namespace'::OnNoMemory",
        ], [
          "chrome_child.dll!blink::reportFatalErrorInMainThread",
          "chrome_child.dll!v8::Utils::ReportApiFailure",
          "chrome_child.dll!v8::Utils::ApiCheck",
          "chrome_child.dll!v8::internal::V8::FatalProcessOutOfMemory",
        ], [
          "chrome_child.dll!WTF::ArrayBuffer::create",
        ], [
          "mozglue.dll!mozalloc_abort",
          "mozglue.dll!mozalloc_handle_oom",
        ], [
          "mozglue.dll!moz_abort",
          "mozglue.dll!pages_commit",
        ], [
          "xul.dll!js::CrashAtUnhandlableOOM",
        ], [
          "xul.dll!NS_ABORT_OOM",
        ], [
          "xul.dll!StatsCompartmentCallback",
        ], [
          "xul.dll!nsGlobalWindow::ClearDocumentDependentSlots",
        ],
      ],
    ),
  },
};

def cErrorReport_foTranslateSpecialErrorReport(oErrorReport, uExceptionCode, oStack):
  # See if we have a translationtable for this exception:
  for (xExceptionCodeOrTypeId, dtxExceptionTranslation) in ddtxExceptionTranslation_xExceptionCodeOrTypeId.items():
    if xExceptionCodeOrTypeId in (oErrorReport.sErrorTypeId, uExceptionCode):
    
  # No match; no translation
  return oErrorReport;
