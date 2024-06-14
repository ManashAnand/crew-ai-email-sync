import React from "react";

const Table = ({ emails }) => {
  return (
    <>
      <div className="  flex justify-center items-center mt-12">
        <div class="relative overflow-x-auto w-4/5">
          <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
              <tr>
                <th scope="col" class="px-6 py-3">
                  Email ID
                </th>
                <th scope="col" class="px-6 py-3">
                  Thread ID
                </th>
                <th scope="col" class="px-6 py-3">
                  Snippet
                </th>
                <th scope="col" class="px-6 py-3">
                  Sender
                </th>
              </tr>
            </thead>
            <tbody>
              {emails?.data?.map((item) => {
                return (
                  <>
                    <tr class="bg-white dark:bg-gray-800">
                      <th
                        scope="row"
                        class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                      >
                        {item?.ID}
                      </th>
                      <td class="px-6 py-4">{item?.threadId}</td>
                      <td class="px-6 py-4">{item?.snippet}</td>
                      <td class="px-6 py-4">{item?.sender}</td>
                    </tr>
                  </>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
};

export default Table;
