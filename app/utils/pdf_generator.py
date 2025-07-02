from fpdf import FPDF
import os
import datetime

class SiswaPDF(FPDF):
    def header(self):
        """Create PDF header with logo"""
        # Logo path
        logo_path = os.path.join('static', 'images', 'school-logo.png')
        
        # If logo exists, add it
        if os.path.exists(logo_path):
            self.image(logo_path, 10, 8, 25)
            start_x = 40
        else:
            start_x = 10
            
        # Header title
        self.set_font('Arial', 'B', 16)
        self.cell(start_x)  # Move to the right from the logo
        self.cell(0, 10, 'UNIVERSITAS TEKNOLOGI INDONESIA', 0, 0, 'C')
        self.ln(7)
        
        # Sub-title
        self.set_font('Arial', '', 12)
        self.cell(start_x)
        self.cell(0, 10, 'DAFTAR SISWA TERDAFTAR', 0, 0, 'C')
        self.ln(20)
        
        # Add a decorative line
        self.set_draw_color(0, 123, 255)
        self.set_line_width(0.5)
        self.line(10, 30, 200, 30)
        
    def footer(self):
        """Create PDF footer with page numbers"""
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Select Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Add page number and timestamp
        self.cell(0, 10, f'Halaman {self.page_no()}/{{nb}} - Dicetak pada: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}', 0, 0, 'C')

def generate_siswa_pdf(siswa_list):
    """
    Generate a PDF with the list of students
    
    Args:
        siswa_list: List of student dictionaries
        
    Returns:
        PDF file as BytesIO object
    """
    from io import BytesIO
    
    # Initialize PDF
    pdf = SiswaPDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    # Add title and metadata
    pdf.set_title('Daftar Siswa')
    pdf.set_author('Universitas Teknologi Indonesia')
    
    # Table header
    pdf.set_font('Arial', 'B', 10)
    pdf.set_fill_color(33, 150, 243)  # Blue header
    pdf.set_text_color(255, 255, 255)  # White text
    
    # Column widths
    col_widths = [10, 40, 30, 25, 25, 30, 30]
    
    # Header titles
    headers = ['No', 'Nama Lengkap', 'Email', 'Telepon', 'Tgl Lahir', 'Asal Sekolah', 'Jurusan']
    
    # Print header
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, 1, 0, 'C', True)
    pdf.ln()
    
    # Table data
    pdf.set_font('Arial', '', 9)
    pdf.set_text_color(0, 0, 0)  # Black text
    
    # Alternate row colors
    alt_colors = [
        (255, 255, 255),  # White
        (240, 248, 255)   # Light blue
    ]
    
    for i, siswa in enumerate(siswa_list):
        # Set row color
        row_color = alt_colors[i % 2]
        pdf.set_fill_color(*row_color)
        
        # Row number
        pdf.cell(col_widths[0], 8, str(i+1), 1, 0, 'C', True)
        
        # Student data
        pdf.cell(col_widths[1], 8, siswa.get('nama_lengkap', ''), 1, 0, 'L', True)
        pdf.cell(col_widths[2], 8, siswa.get('email', '')[:20], 1, 0, 'L', True)
        pdf.cell(col_widths[3], 8, siswa.get('no_telepon', ''), 1, 0, 'L', True)
        
        # Format tanggal lahir
        tanggal_lahir = siswa.get('tanggal_lahir', '')
        if isinstance(tanggal_lahir, datetime.date):
            tanggal_lahir = tanggal_lahir.strftime('%d-%m-%Y')
        
        pdf.cell(col_widths[4], 8, str(tanggal_lahir), 1, 0, 'L', True)
        pdf.cell(col_widths[5], 8, siswa.get('asal_sekolah', '')[:20], 1, 0, 'L', True)
        pdf.cell(col_widths[6], 8, siswa.get('jurusan_pilihan', '')[:15], 1, 0, 'L', True)
        
        pdf.ln()
    
    # Add total number of students
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 10, f"Total Siswa: {len(siswa_list)}", 0, 1)
    
    # Output to BytesIO
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)
    
    return pdf_output
