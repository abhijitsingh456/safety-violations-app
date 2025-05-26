Vue.createApp({
    data() {
        return {
            isSidebarCollapsed: true,
            topN: 5,
            violationCount: 1,
            startDate: '',
            endDate: '',
            speed: 30,
            employees: [],
            selectedEmployees: [],
            selectAll: false
        };
    },
    methods: {
        toggleSidebar() {
            this.isSidebarCollapsed = !this.isSidebarCollapsed;
        },
        async fetchData() {
            const url=`/api/get_no_of_speed_violations/${this.startDate}/${this.endDate}/${this.violationCount}/${this.speed}/`
            try{
                const response = await fetch(url)
                if (!response.ok){
                    throw new Error(`Respose Status: ${response.status}`)
                }
            rawData = await response.json();
            this.employees = rawData.map(emp => ({ ...emp }));
            this.selectedEmployees = []; // reset selections
            this.selectAll = false;
            }catch(error){
                console.error(error.message)
            }
        },
        toggleSelectAll() {
            if (this.selectAll) {
            this.selectedEmployees = [...this.employees];
            } else {
            this.selectedEmployees = [];
            }
        },
        submitSelected() {
            // Simulate an API call
            console.log("Submitting selected employees:", this.selectedEmployees);

            // Example POST logic (mocked):
            // fetch('/api/submit', {
            //   method: 'POST',
            //   headers: { 'Content-Type': 'application/json' },
            //   body: JSON.stringify(this.selectedEmployees)
            // })

            alert(`Submitted ${this.selectedEmployees.length} selected entries!`);
        },
        downloadExcel() {
            const wb = XLSX.utils.book_new();
            const wsData = [
                ["Name", "Department", "Designation", "Speed", "Violation Type", "No. of Violations", "Locations"],
                ...this.employees.map(emp => [
                emp.name,
                emp.department,
                emp.designation,
                emp.speed,
                emp.violationType,
                emp.violations,
                emp.locations
                ])
            ];

            const ws = XLSX.utils.aoa_to_sheet(wsData);
            XLSX.utils.book_append_sheet(wb, ws, "Violations");
            XLSX.writeFile(wb, "employee_violations.xlsx");
        }
    },
    mounted() {
        flatpickr(this.$refs.startDate, {
            dateFormat: "Y-m-d",
            onChange: ([selectedDate]) => {
              this.startDate = selectedDate.toISOString().split('T')[0]; // get only date
            }
          });
    
          flatpickr(this.$refs.endDate, {
            dateFormat: "Y-m-d",
            onChange: ([selectedDate]) => {
              this.endDate = selectedDate.toISOString().split('T')[0]; // get only date
            }
          });
      },
      delimiters: ['[[', ']]']
}).mount("#app");
