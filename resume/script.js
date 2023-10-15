// Toggle between online and PDF versions

function generatePDF() {
const onlineVersion = document.getElementById('contact');
const pdfVersion = document.getElementById('contact-pdf');
const pdfButton = document.getElementById('pdf-button');

const options = {
	margin: [15,15],
	filename: `RamiroGarcia_${getCurrentDate()}.pdf`,
	image:        { type: 'jpeg', quality: 0.98 },
	html2canvas:  { scale: 2, letterRendering: true },
	jsPDF:        { unit: 'pt', format: 'letter', orientation: 'portrait' },
	pagebreak: { mode: ['avoid-all', 'css', 'legacy'] }
	
};

onlineVersion.style.display = 'none';
pdfVersion.style.display = 'block';
pdfButton.style.display = 'none';

// Choose the element id which you want to export.
var element = document.body;

// Choose the element and pass it to html2pdf() function and call the save() on it to save as pdf.
html2pdf().set(options).from(element).save();
}

function getCurrentDate() {
	const today = new Date();
	const year = today.getFullYear();
	const month = String(today.getMonth() + 1).padStart(2, '0');
	const day = String(today.getDate()).padStart(2, '0');
	return `${year}-${month}-${day}`;
}