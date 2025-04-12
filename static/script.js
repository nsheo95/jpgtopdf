document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("upload-form");
    const downloadSection = document.getElementById("download-section");
    const downloadLink = document.getElementById("download-link");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const formData = new FormData(form);

        try {
            const response = await fetch("/convert", {
                method: "POST",
                body: formData,
            });

            if (!response.ok) {
                throw new Error("서버 오류 발생");
            }

            const blob = await response.blob();

            // 임시 URL 생성 후 다운로드 링크에 연결
            const url = window.URL.createObjectURL(blob);
            downloadLink.href = url;
            downloadLink.download = "converted.pdf";

            // 다운로드 섹션 표시
            downloadSection.style.display = "block";
        } catch (error) {
            alert("PDF 변환에 실패했습니다. 다시 시도해주세요.");
            console.error(error);
        }
    });
});
