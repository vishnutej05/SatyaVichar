chrome.runtime.onInstalled.addListener(function() {
    chrome.contextMenus.create({
      title: "Search with our model",
      contexts: ["selection"],
      id: "fakeNewsDetector"
    });
  });
  

  chrome.contextMenus.onClicked.addListener(function(info, tab) {
    if (info.menuItemId === "fakeNewsDetector") {
      const selectedText = info.selectionText;
      chrome.storage.local.set({ 'selectedText': selectedText }, function() {
        console.log('Selected text stored:', selectedText);
      });
    }
  });



//   Sending user news to python
