function pageFunction(context) {
  const $ = context.jQuery;
  const regex = /Typ\sškoly:\s?([A-zÀ-Ž]*),?\s?(.*)Ředitel\/ka:\s?(.+)/;

  $(".advertise").remove();
  return $(".doc_entry_desc")
    .map((_, el) => {
      const name = $(el).find(".school_name a").text();
      const info = $(el).find(".school_info").text();
      let result;
      const dataResult = info.match(regex);

      if (dataResult) {
        if (dataResult.length >= 4) {
          const splitResult = dataResult[3].split(",");
          result = [...dataResult, ...splitResult];
        }
      } else {
        result = [];
      }
      return {
        name,
        result,
      };
    })
    .toArray();
}